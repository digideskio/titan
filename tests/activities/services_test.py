#!/usr/bin/env python
# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for services.py."""

from tests.common.lib import endpointstest

from titan.common.lib.google.apputils import basetest
from titan import endpoints
from titan.activities import messages
from titan.activities import services

class ServicesTest(endpointstest.EndpointsTestCase):

  def setUp(self):
    super(ServicesTest, self).setUp()
    self.service = self.GetServiceStub(services.ActivitiesService)

  def CreateWsgiApplication(self):
    """Returns the wsgi application for the service endpoint testing."""
    return endpoints.EndpointsApplication([services.ActivitiesService],
                                          restricted=False)

  def testGetActivities(self):
    request = messages.GetActivitiesRequest()
    self.assertEquals(messages.GetActivitiesResponse(),
                      self.service.get_activities(request))

if __name__ == '__main__':
  basetest.main()
