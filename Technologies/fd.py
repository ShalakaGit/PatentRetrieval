# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 03:48:05 2017

@author: Shalaka
"""

import os
from nltk.probability import FreqDist, ConditionalFreqDist
import numpy as np
import math

class NaiveBayes:

    def main(self):
        trainFile = 'E:\\NLP\\assignment4\\assignment4\\data\\train'
        testFile = 'E:\\NLP\\assignment4\\assignment4\\data\\test'
        dataSplit,speakers = self.LoadData(trainFile)
        testData,speakers = self.LoadData(testFile)
        speakersWords = {}
        documentCounts = {}
        for _ in dataSplit:
            documentCounts[_] = len(dataSplit[_])
        #with open('documentCounts.txt','w') as f:
        #    for count in documentCounts:
        #        f.write(count+":"+ str(documentCounts[count]))
        #        f.write('\n')
        #        print(count)
        #        print(documentCounts[count])
        for speaker in dataSplit:
            for line in dataSplit[speaker]:
                    words = line.split(' ')
                    if '.' in words:
                        words.remove('.')
                    if ',' in words:
                        words.remove(',')
                    if speaker in speakersWords:
                        speakersWords[speaker].append(words)
                    else:
                        speakersWords[speaker] = [words]
        with open('wordCounts.txt','w') as f:
            for _ in speakersWords:
                count= 0
                for collect in speakersWords[_]:
                    collect = set(collect)
                    count = count + len(collect)
        train_Unigram = {}
        for speaker in speakersWords:
            for collect in speakersWords[speaker]:
                if speaker in train_Unigram:
                    for element in collect:
                        train_Unigram[speaker].append(element)
                else:
                    train_Unigram[speaker] = collect
        i = 0
        g =globals()


        for element in train_Unigram:
            x = NaiveBayes.CalcProbabilities(FreqDist(train_Unigram[element]))
            train_Unigram[element] = x

        results = []
        correct = 0
        count = 0
        i = -1
        for speaker in testData:
            i +=1
            count = 0
            correct=0
            for documents in testData[speaker]:
                count += 1
                probabilities = self.Classify(train_Unigram,documents)
                maxVal = max(probabilities)
                if probabilities.index(maxVal) == i or probabilities.index(maxVal) == (i+1) or (i-1):
                    correct +=1
            print('Correct Predictions',correct/count)
            results.append(correct/count)

        print('Total Accuracy',sum(results)/len(results))

    def CalcProbabilities(wordList):
        N = len(wordList)
        vocab = set(wordList)
        for word in wordList:
            count = wordList[word] + 1        # Add one smoothing
            probability = np.divide(count,(N+1.0*(len(vocab))))
            wordList[word] = math.log(probability,math.e)
        return wordList

    def LoadData(self,fileName):
        dataSplit = {}
        speakers = []
        with open(fileName, 'r') as f:
            data = f.read()
            for line in data.split('\n'):
                if not line:
                    break
                else:
                    name = line.split(' ', 1)[0]
                    if (len(line.split(' ')) >= 1):
                        words = line.split(' ', 1)[1]
                        speakers.append(name)
                        if name in dataSplit:
                            dataSplit[name].append(words)
                        else:
                            dataSplit[name] = [words]
                    else:
                        continue

            speakers = set(speakers)
        return dataSplit,speakers

    def Classify(self,train,test):
        probabilities = []
        for document in test.split('\n'):
            for speaker in train:
                P_doc = 0.0
                vocab = len(train[speaker])
                for word in document.split(' '):
                    if word in train[speaker]:
                        P_doc = P_doc + train[speaker][word]
                    else:
                        P_doc = P_doc+ math.log(1.0/vocab)
                probabilities.append(P_doc)
        return probabilities

b = NaiveBayes()
b.main()