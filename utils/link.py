# -*- coding: utf-8 -*-
# Copyright (c) 2013, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#     Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#     Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#     Neither the name of the <ORGANIZATION> nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

def link(pyxb_class, dflt=False):
    """ Create an initialization link between the pyxb class and the subClass implementation.
        Typical use is as a decorator:
            @link.link(pyxb_class)
            class subClass(pyxb_class, ...):

        If loading from XML (_from_xml is an attribute), this invokes the pyxb initializer
        which then invokes the validateBinding method

        Otherwise, it calls the normal initializer
    """

    def model_link(model_class):
        orig_init = model_class.__init__
        orig_new  = model_class.__new__

        @staticmethod
        def __new__(cls, *kw, **kwargs):
            if kwargs.get('_from_xml') or kwargs.get('_raw'):
                return pyxb_class.__new__(cls, *kw, **kwargs)
            return orig_new(cls, *kw, **kwargs)


        def __init__(self, *kw, **kwargs):
            if '_from_xml' in kwargs or '_raw' in kwargs:
                if '_raw' in kwargs: del kwargs['_raw']
                pyxb_class.__init__(self, *kw, **kwargs)
            else:
                if dflt: pyxb_class.__init__(self)
                orig_init(self, *kw, **kwargs)

        # TODO: This doesn't work for non-element entries.  We need to talk to the pyxb folks
        #       about a generic clone mechanism.
        # model_class.clone = lambda x: core_api.CreateFromDocument(x.toxml().encode('utf-8'))

        model_class.__init__ = __init__
        model_class.__new__  = __new__
        pyxb_class._SetSupersedingClass(model_class)
        return model_class

    return model_link


def linkd(pyxb_class):
    return link(pyxb_class, True)
