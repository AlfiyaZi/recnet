from __future__ import absolute_import, print_function, division
"""
This file contains a super class for all layers
"""

######                           Imports
########################################
from abc import ABCMeta, abstractmethod
import numpy as np
import theano
import theano.tensor as T
from past.builtins import xrange

class LayerMaster(object):

    __metaclass__ = ABCMeta


    ###### Abstract sequenceiteration method
    ########################################
    @abstractmethod
    def sequence_iteration(self):
        pass

    def sigmoid(self):
        return T.nnet.hard_sigmoid # sigmoid # T.nnet.hard_sigmoid #T.nnet.sigmoid

    def ln(self, x, b, s):
        _eps = 1e-5
        output = (x - x.mean(1)[:,None]) / T.sqrt((x.var(1)[:,None] + _eps))
        output = s[None, :] * output + b[None,:]
        return output

    def sqr_ortho(self, rng, ndim):
        W = rng.randn(ndim, ndim)
        u, s, v = np.linalg.svd(W)
        return u.astype(T.config.floatX)

    def rec_ortho(self, rng, ndim, ndim_factor):
        W = np.concatenate([self.sqr_ortho(rng, ndim) for i in xrange(ndim_factor)], axis=1)
        return W

    def rec_uniform_sqrt(self, rng, ndimA, ndimB):
        return rng.uniform(-np.sqrt(1./ndimB), np.sqrt(1./ndimB), (int(ndimA),int(ndimB)))

    def rec_uniform_const(self, rng, ndimA, ndimB):
        return rng.uniform(-0.1,0.1, (ndimA, ndimB))

    def rec_normal_const(self, rng, ndimA, ndimB):
        return rng.normal(0, 2./(ndimA+ndimB), (ndimA, ndimB))

    def vec_uniform_sqrt(self, rng, ndim):
        return rng.uniform(-np.sqrt(1./ndim), np.sqrt(1./ndim), ndim)

    def vec_uniform_const(self, rng, ndim):
        return rng.uniform(-0.1,0.1, ndim)

    def vec_normal_const(self, rng, ndim):
        return  rng.normal(0, 1./(ndim), ndim)








