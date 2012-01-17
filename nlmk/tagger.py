# -*- coding: utf-8 -*-

_ext = {
  u'јќи':'GP', # глаголски прилог
  u'ува':'NSV', # несвојствен глагол
  u'увал':'NSVL', # несвојствен глагол, л-форма
  u'увала':'NSVL',
  u'увале':'NSVL',
  u'увало':'NSVL',
  u'дил':'GL', # глагол, л-форма
  u'дила':'GL', # глагол, л-форма
  u'диле':'GL', # глагол, л-форма
  u'дило':'GL', # глагол, л-форма
  u'ше':'NSV',
  u'аат':'GP3', # глагол, плурал, 3лице,
  u'ениот':'PRMC',   # придавка, машки род, член
  u'чните':'PRPC',  # придавка, плурал, множина
  u'чни':'PRP', # придавка, плурал 
  u'ник':'IM', # именка, машки род
  u'риот':'PR',  # придавка
  u'рата':'PR',  # придавка
  u'рите':'PR',  # придавка
  u'ање':'GI',    # глаголска именка
  u'дачи':'IM',
  u'цачи':'IM'
  #u'ици':'I' # именка
}

_exact = {
  'PU':list(u',.[]()"„“`\';:!?'),
  'PR':[u'мој', u'мои',u'моја',u'мое',u'мојот',u'мојата',u'моето',u'моите',
        u'твој',u'твои',u'твоја',u'твое',u'твојот',u'твоите',u'твојата',u'твоето',
        u'негов',u'негова',u'негово',u'негови',u'неговиот',u'неговата',u'неговото',u'неговите',
        u'нејзин',u'нејзина',u'нејзино',u'нејзини',u'нејзиниот',u'нејзината',u'нејзиното',u'нејзините',
        u'наш',u'наша',u'наше',u'наши',u'нашиот',u'нашата',u'нашето',u'нашите',
        u'ваш',u'ваше',u'веша',u'ваши',u'вашиот',u'вашето',u'вешата',u'вашите',
        u'нивен',u'нивна',u'нивно',u'нивни',u'нивниот',u'нивната',u'нивното',u'нивните']
          
}

def tag(token):
    for tag_, vals in _exact.iteritems():
        if token in vals:
            return tag_
    for ext, tag_ in _ext.iteritems():
        if token.endswith(ext):
            return tag_
    
    return None

