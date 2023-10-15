from flask import Flask, abort
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)
api = Api(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'site.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<VideoModel(name={self.name}, views={self.views}, likes={self.likes})>"

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

video_patch_args = reqparse.RequestParser()
video_patch_args.add_argument("name", type=str, help="Name of the video")
video_patch_args.add_argument("views", type=int, help="Views of the video")
video_patch_args.add_argument("likes", type=int, help="Likes on the video")


resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}
# videos = {}

# def abort_if_video_none(video_id):
#     if video_id not in videos:
#         abort(404, "Could not find video with that ID..")

# def abort_if_video_exists(video_id):
#     if video_id in videos:
#         abort(409, "Video with that ID exists..")

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.get(video_id)
        if not result:
            abort(404, "Could not find any video with that ID in Database.")
        # Research resource field for serialization to Json
        return result
        # abort_if_video_none(video_id)
        # return videos[video_id]
    
    @marshal_with(resource_fields)
    def put(self, video_id):
        # abort_if_video_exists(video_id)
        # args = video_put_args.parse_args()
        # videos[video_id] = args                     
        # return videos[video_id], 201 #201-Created

        result = VideoModel.query.get(video_id)
        if result:
            abort(409, "Video ID already exists. Please choose a different ID")

        args = video_put_args.parse_args()
        video = VideoModel(id=video_id, name=args['name'],
                            views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()

        return video, 201

    def delete(self, video_id):
        # abort_if_video_none(video_id)
        # del videos[video_id]
        result = VideoModel.query.get(video_id)

        return '', 204
    
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_patch_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()

        if not result:
            abort(404, "Could not find any video with that ID in Database.")

        for arg in args:
            if args[arg] and arg in result.__dict__:
                exec(f'result.{arg} = {args[arg]}')
        db.session.commit()

        return result
    
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)