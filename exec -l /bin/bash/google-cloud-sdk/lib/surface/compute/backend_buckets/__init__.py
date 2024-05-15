# -*- coding: utf-8 -*- #
# Copyright 2015 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Commands for reading and manipulating backend buckets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base


class BackendBuckets(base.Group):
  """Read and manipulate backend buckets.

  Backend buckets define Cloud Storage buckets that can serve content.
  URL maps define which requests are sent to which backend buckets. For more
  information, see:
  https://cloud.google.com/load-balancing/docs/https/ext-load-balancer-backend-buckets.
  """


BackendBuckets.category = base.LOAD_BALANCING_CATEGORY

BackendBuckets.detailed_help = {
    'DESCRIPTION': """
        Read and manipulate backend buckets. Backend buckets define Cloud
        Storage buckets that can serve content. URL maps define which
        requests are sent to which backend buckets.

        For more information about backend buckets, see the
        [backend buckets documentation](https://cloud.google.com/load-balancing/docs/https/ext-load-balancer-backend-buckets).

        See also: [Backend buckets API](https://cloud.google.com/compute/docs/reference/rest/v1/backendBuckets).
    """,
}
