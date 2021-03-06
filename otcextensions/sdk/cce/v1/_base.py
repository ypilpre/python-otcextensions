# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from openstack import resource

from otcextensions.sdk import sdk_resource


class Metadata(sdk_resource.Resource):

    # Properties
    #: UUID
    #: *Type:str
    id = resource.Body('uuid', alternate_id=True)
    #: Name
    #: *Type:str
    name = resource.Body('name')
    #: Space UUID
    #: *Type:str
    space_uuid = resource.Body('spaceuuid')
    #: Create time
    #: *Type:str
    create_time = resource.Body('createAt')
    #: Update time
    #: *Type:str
    update_time = resource.Body('updateAt')


class Resource(sdk_resource.Resource):
    base_path = ''

    service_expectes_json_type = True

    # Properties
    #: Kind
    kind = resource.Body('kind')
    #: api version
    api_version = resource.Body('apiVersion', default='v1')
    #: metadata
    metadata = resource.Body('metadata', type=Metadata)
