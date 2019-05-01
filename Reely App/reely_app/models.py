from datetime import datetime
from flask import current_app
from reely_app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)

Posts = [
  {
    'article_id': 1,
    'article_published': 1545730073,
    'article_tags': [
      {
        'slug': 'tag-1',
        'name': 'Tag 1'
      },
      {
        'slug': 'tag-2',
        'name': 'Tag 2'
      },
      {
        'slug': 'tag-3',
        'name': 'Tag 3'
      }
    ],
    'article_group': 1,
    'article_sub_group': 1,
    'article_title': ' Article Title 1-1',
    'article_video': '<iframe src="https://www.youtube.com/embed/ScMzIvxBSi4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    'article_featured_image': {
      'ait_text': 'Image 1 Alt Text',
      'img_src': '../static/img/image_1.jpg'
     },
    'article_body': '<h2>Lorem ipsum dolor sit amet, consectetur</h2><p>Lorem ipsum dolor sit amet consectetur</h2><p>Lorem ipsum dolor sit amet</p>',
    'article_description': 'Fuscenectellussedauguesemperporta</b>.Aeneanquam.Inscelerisquesematdolor.<b>Maurismassa</b>.Maecenasmattis.Sedconvallistristiquesem.Proinutligulavelnuncegestasporttitor.Morbilectusrisus,iaculisvel,suscipitquis,luctusnon,massa.Fusceacturpisquisligulalaciniaaliquet.Maurisipsum',
    'article_notes': '<h3>RelavantLinks:</h3><ul><li><ahref="#">HubspotvideoDocumentation</a></li><li><ahref="#">YoutubeiframeInstructions</a></li><li><ahref="#">W3SchoolsiframeExamples</a></li></ul><h3>Repos:</h3><ul><li><ahref="#">StrippedYoutubeiframecode</a></li></ul>'
  },
  {
    'article_id': 2,
    'article_published': 1545730073,
    'article_tags': [
      {
        'slug': 'tag-1',
        'name': 'Tag 1'
      },
      {
        'slug': 'tag-2',
        'name': 'Tag 2'
      },
      {
        'slug': 'tag-3',
        'name': 'Tag 3'
      }
    ],
    'article_group': 2,
    'article_sub_group': 1,
    'article_title': 'Article Title 2-1',
    'article_video': '<iframesrc="https://www.youtube.com/embed/ScMzIvxBSi4"frameborder="0"allow="accelerometer;autoplay;encrypted-media;gyroscope;picture-in-picture"allowfullscreen></iframe>',
    'article_featured_image': {
      'ait_text': 'Image 1 Alt Text',
      'img_src': '../static/img/image_1.jpg'
     },
    'article_body': '<h2>Lorem ipsum dolor sit amet, consectetur</h2><p>Lorem ipsum dolor sit amet consectetur</h2><p>Lorem ipsum dolor sit amet</p>',
    'article_description': 'Fuscenectellussedauguesemperporta</b>.Aeneanquam.Inscelerisquesematdolor.<b>Maurismassa</b>.Maecenasmattis.Sedconvallistristiquesem.Proinutligulavelnuncegestasporttitor.Morbilectusrisus,iaculisvel,suscipitquis,luctusnon,massa.Fusceacturpisquisligulalaciniaaliquet.Maurisipsum',
    'article_notes': '<h3>RelavantLinks:</h3><ul><li><ahref="#">HubspotvideoDocumentation</a></li><li><ahref="#">YoutubeiframeInstructions</a></li><li><ahref="#">W3SchoolsiframeExamples</a></li></ul><h3>Repos:</h3><ul><li><ahref="#">StrippedYoutubeiframecode</a></li></ul>'
  }
]