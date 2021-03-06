#!/usr/bin/env python3

# custom imports
from app import app, api, mongo
from resources import resources as res


api.add_resource(res.UserSignup, '/signup')
api.add_resource(res.UserSignin, '/signin')
api.add_resource(res.TokenRefresh, '/token/refresh')

api.add_resource(res.ConfirmToken, '/confirm')
api.add_resource(res.ChangePassword, '/change')
api.add_resource(res.ResetPassword, '/reset')

api.add_resource(res.User, '/user', '/user/<string:id>')
api.add_resource(res.UserList, '/user/list')
api.add_resource(res.UserAvatar, '/user/avatar/<string:id>')
api.add_resource(res.UserProfile, '/user/profile/<string:id>')
api.add_resource(res.UserLastseen, '/user/lastseen/<string:id>')
api.add_resource(res.UserChangePassword, '/user/change/<string:id>')
api.add_resource(res.UserDeleteAccount, '/user/delete/account')
api.add_resource(res.UserChallenge, '/user/challenge')
api.add_resource(res.UserExport, '/user/export')

api.add_resource(res.Challenge, '/challenge', '/challenge/<string:id>')
api.add_resource(res.ChallengeList, '/challenge/list')
api.add_resource(res.ChallengeSubscription, '/challenge/subscription')
api.add_resource(res.ChallengeSubscriptionList, '/challenge/subscription/list')
api.add_resource(res.ChallengeExport, '/challenge/export')
api.add_resource(res.ChallengeTask, '/challenge/task',
                 '/challenge/task/<string:id>')
api.add_resource(res.ChallengeTaskDetail, '/challenge/task/detail',
                 '/challenge/task/detail/<string:id>')
api.add_resource(res.ChallengeTaskProgress, '/challenge/task/progress')
api.add_resource(res.ChallengeTaskFormExport, '/challenge/task/form/export')
api.add_resource(res.ChallengeTaskResponseExport,
                 '/challenge/task/response/export')
api.add_resource(res.ChallengeTaskResponse, '/challenge/task/response',
                 '/challenge/task/response/<string:id>')
api.add_resource(res.ChallengeTaskFormList, '/challenge/task/form/list')
api.add_resource(res.ChallengeTaskForm, '/challenge/task/form',
                 '/challenge/task/form/<string:id>')
api.add_resource(res.ChallengeRequestList, '/challenge/request/list')
api.add_resource(res.ChallengeRequest, '/challenge/request',
                 '/challenge/request/<string:id>')

api.add_resource(res.MailTemplate, '/template', '/template/<string:id>')
api.add_resource(res.MailTemplateList, '/template/list')

api.add_resource(res.WikiEntry, '/wiki/entry', '/wiki/entry/<string:id>')
api.add_resource(res.WikiEntryTag, '/wiki/entry/tag')
api.add_resource(res.WikiEntrySearch, '/wiki/entry/search')
api.add_resource(res.WikiEntryList, '/wiki/entry/list')

api.add_resource(res.LandingPage, '/landing')
api.add_resource(res.Fetch, '/fetch')


# create index on collections
mongo.db.users.create_index([('email', 1)], unique=True)
mongo.db.entries.create_index([('title', 'text'), ('content', 'text')])


if __name__ == '__main__':
    # print(app.url_map)
    app.run(debug=True)
