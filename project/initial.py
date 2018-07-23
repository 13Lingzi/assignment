# -*- coding: utf-8 -*-
import os
from pyltp import SentenceSplitter
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer
from pyltp import Parser
from project.util import get_config

# import jieba
#分词模型加载
def segmentor_initial():
    cws_model_path = os.path.join(get_config('ner', 'LTP_DATA_DIR'), 'cws.model')  # 分词模型路径，模型名称为`cws.model`
    segmentor = Segmentor()  # 初始化实例
    segmentor.load(cws_model_path)  # 加载模型
    # segmentor.load_with_lexicon(cws_model_path, get_config('ner', 'lexicon'))  # 加载模型
    return segmentor

#词性标注模型加载
def postagger_initial():
    pos_model_path = os.path.join(get_config('ner', 'LTP_DATA_DIR'), 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
    postagger = Postagger()  # 初始化实例
    postagger.load(pos_model_path)  # 加载模型
    return postagger


#实体识别模型加载
def recognizer_initial():
    ner_model_path = os.path.join(get_config('ner', 'LTP_DATA_DIR'), 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`
    recognizer = NamedEntityRecognizer()  # 初始化实例
    recognizer.load(ner_model_path)  # 加载模型
    return recognizer

def parser_initial():
    par_model_path = os.path.join(get_config('ner', 'LTP_DATA_DIR'), 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`
    parser = Parser()  # 初始化实例
    parser.load(par_model_path)  # 加载模型
    return parser

#模型释放
def release_model(segmentor,postagger,recognizer):
    segmentor.release()  # 释放模型
    postagger.release()  # 释放模型
    recognizer.release()  # 释放模型