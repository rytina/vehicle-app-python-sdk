# -*- coding: utf-8 -*-
# Copyright (c) 2022 Robert Bosch GmbH and Microsoft Corporation
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chariott/runtime/v1/runtime.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sdv.proto.chariott.common.v1 import (
    common_pb2 as chariott_dot_common_dot_v1_dot_common__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n!chariott/runtime/v1/runtime.proto\x12\x13\x63hariott.runtime.v1\x1a\x1f\x63hariott/common/v1/common.proto"\xec\x01\n\x19IntentServiceRegistration\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12R\n\x08locality\x18\x04 \x01(\x0e\x32@.chariott.runtime.v1.IntentServiceRegistration.ExecutionLocality"O\n\x11\x45xecutionLocality\x12\x1c\n\x18\x45XECUTION_LOCALITY_LOCAL\x10\x00\x12\x1c\n\x18\x45XECUTION_LOCALITY_CLOUD\x10\x01"R\n\x0f\x41nnounceRequest\x12?\n\x07service\x18\x01 \x01(\x0b\x32..chariott.runtime.v1.IntentServiceRegistration"V\n\x10\x41nnounceResponse\x12\x42\n\x12registration_state\x18\x01 \x01(\x0e\x32&.chariott.runtime.v1.RegistrationState"\x8c\x01\n\x0fRegisterRequest\x12?\n\x07service\x18\x01 \x01(\x0b\x32..chariott.runtime.v1.IntentServiceRegistration\x12\x38\n\x07intents\x18\x02 \x03(\x0b\x32\'.chariott.runtime.v1.IntentRegistration"\x12\n\x10RegisterResponse"\xe6\x01\n\x12IntentRegistration\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12>\n\x06intent\x18\x02 \x01(\x0e\x32..chariott.runtime.v1.IntentRegistration.Intent"}\n\x06Intent\x12\x13\n\x0fINTENT_DISCOVER\x10\x00\x12\x12\n\x0eINTENT_INSPECT\x10\x01\x12\x0f\n\x0bINTENT_READ\x10\x02\x12\x10\n\x0cINTENT_WRITE\x10\x03\x12\x11\n\rINTENT_INVOKE\x10\x04\x12\x14\n\x10INTENT_SUBSCRIBE\x10\x05"O\n\x0e\x46ulfillRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12*\n\x06intent\x18\x02 \x01(\x0b\x32\x1a.chariott.common.v1.Intent"G\n\x0f\x46ulfillResponse\x12\x34\n\x0b\x66ulfillment\x18\x01 \x01(\x0b\x32\x1f.chariott.common.v1.Fulfillment*Y\n\x11RegistrationState\x12 \n\x1cREGISTRATION_STATE_ANNOUNCED\x10\x00\x12"\n\x1eREGISTRATION_STATE_NOT_CHANGED\x10\x01\x32\x99\x02\n\x0f\x43hariottService\x12W\n\x08\x41nnounce\x12$.chariott.runtime.v1.AnnounceRequest\x1a%.chariott.runtime.v1.AnnounceResponse\x12W\n\x08Register\x12$.chariott.runtime.v1.RegisterRequest\x1a%.chariott.runtime.v1.RegisterResponse\x12T\n\x07\x46ulfill\x12#.chariott.runtime.v1.FulfillRequest\x1a$.chariott.runtime.v1.FulfillResponseb\x06proto3'
)

_REGISTRATIONSTATE = DESCRIPTOR.enum_types_by_name["RegistrationState"]
RegistrationState = enum_type_wrapper.EnumTypeWrapper(_REGISTRATIONSTATE)
REGISTRATION_STATE_ANNOUNCED = 0
REGISTRATION_STATE_NOT_CHANGED = 1


_INTENTSERVICEREGISTRATION = DESCRIPTOR.message_types_by_name[
    "IntentServiceRegistration"
]
_ANNOUNCEREQUEST = DESCRIPTOR.message_types_by_name["AnnounceRequest"]
_ANNOUNCERESPONSE = DESCRIPTOR.message_types_by_name["AnnounceResponse"]
_REGISTERREQUEST = DESCRIPTOR.message_types_by_name["RegisterRequest"]
_REGISTERRESPONSE = DESCRIPTOR.message_types_by_name["RegisterResponse"]
_INTENTREGISTRATION = DESCRIPTOR.message_types_by_name["IntentRegistration"]
_FULFILLREQUEST = DESCRIPTOR.message_types_by_name["FulfillRequest"]
_FULFILLRESPONSE = DESCRIPTOR.message_types_by_name["FulfillResponse"]
_INTENTSERVICEREGISTRATION_EXECUTIONLOCALITY = (
    _INTENTSERVICEREGISTRATION.enum_types_by_name["ExecutionLocality"]
)
_INTENTREGISTRATION_INTENT = _INTENTREGISTRATION.enum_types_by_name["Intent"]
IntentServiceRegistration = _reflection.GeneratedProtocolMessageType(
    "IntentServiceRegistration",
    (_message.Message,),
    {
        "DESCRIPTOR": _INTENTSERVICEREGISTRATION,
        "__module__": "chariott.runtime.v1.runtime_pb2"
        # @@protoc_insertion_point(class_scope:chariott.runtime.v1.IntentServiceRegistration)
    },
)
_sym_db.RegisterMessage(IntentServiceRegistration)

AnnounceRequest = _reflection.GeneratedProtocolMessageType(
    "AnnounceRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _ANNOUNCEREQUEST,
        "__module__": "chariott.runtime.v1.runtime_pb2"
        # @@protoc_insertion_point(class_scope:chariott.runtime.v1.AnnounceRequest)
    },
)
_sym_db.RegisterMessage(AnnounceRequest)

AnnounceResponse = _reflection.GeneratedProtocolMessageType(
    "AnnounceResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _ANNOUNCERESPONSE,
        "__module__": "chariott.runtime.v1.runtime_pb2"
        # @@protoc_insertion_point(class_scope:chariott.runtime.v1.AnnounceResponse)
    },
)
_sym_db.RegisterMessage(AnnounceResponse)

RegisterRequest = _reflection.GeneratedProtocolMessageType(
    "RegisterRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _REGISTERREQUEST,
        "__module__": "chariott.runtime.v1.runtime_pb2"
        # @@protoc_insertion_point(class_scope:chariott.runtime.v1.RegisterRequest)
    },
)
_sym_db.RegisterMessage(RegisterRequest)

RegisterResponse = _reflection.GeneratedProtocolMessageType(
    "RegisterResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _REGISTERRESPONSE,
        "__module__": "chariott.runtime.v1.runtime_pb2"
        # @@protoc_insertion_point(class_scope:chariott.runtime.v1.RegisterResponse)
    },
)
_sym_db.RegisterMessage(RegisterResponse)

IntentRegistration = _reflection.GeneratedProtocolMessageType(
    "IntentRegistration",
    (_message.Message,),
    {
        "DESCRIPTOR": _INTENTREGISTRATION,
        "__module__": "chariott.runtime.v1.runtime_pb2"
        # @@protoc_insertion_point(class_scope:chariott.runtime.v1.IntentRegistration)
    },
)
_sym_db.RegisterMessage(IntentRegistration)

FulfillRequest = _reflection.GeneratedProtocolMessageType(
    "FulfillRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _FULFILLREQUEST,
        "__module__": "chariott.runtime.v1.runtime_pb2"
        # @@protoc_insertion_point(class_scope:chariott.runtime.v1.FulfillRequest)
    },
)
_sym_db.RegisterMessage(FulfillRequest)

FulfillResponse = _reflection.GeneratedProtocolMessageType(
    "FulfillResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _FULFILLRESPONSE,
        "__module__": "chariott.runtime.v1.runtime_pb2"
        # @@protoc_insertion_point(class_scope:chariott.runtime.v1.FulfillResponse)
    },
)
_sym_db.RegisterMessage(FulfillResponse)

_CHARIOTTSERVICE = DESCRIPTOR.services_by_name["ChariottService"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _REGISTRATIONSTATE._serialized_start = 1052
    _REGISTRATIONSTATE._serialized_end = 1141
    _INTENTSERVICEREGISTRATION._serialized_start = 92
    _INTENTSERVICEREGISTRATION._serialized_end = 328
    _INTENTSERVICEREGISTRATION_EXECUTIONLOCALITY._serialized_start = 249
    _INTENTSERVICEREGISTRATION_EXECUTIONLOCALITY._serialized_end = 328
    _ANNOUNCEREQUEST._serialized_start = 330
    _ANNOUNCEREQUEST._serialized_end = 412
    _ANNOUNCERESPONSE._serialized_start = 414
    _ANNOUNCERESPONSE._serialized_end = 500
    _REGISTERREQUEST._serialized_start = 503
    _REGISTERREQUEST._serialized_end = 643
    _REGISTERRESPONSE._serialized_start = 645
    _REGISTERRESPONSE._serialized_end = 663
    _INTENTREGISTRATION._serialized_start = 666
    _INTENTREGISTRATION._serialized_end = 896
    _INTENTREGISTRATION_INTENT._serialized_start = 771
    _INTENTREGISTRATION_INTENT._serialized_end = 896
    _FULFILLREQUEST._serialized_start = 898
    _FULFILLREQUEST._serialized_end = 977
    _FULFILLRESPONSE._serialized_start = 979
    _FULFILLRESPONSE._serialized_end = 1050
    _CHARIOTTSERVICE._serialized_start = 1144
    _CHARIOTTSERVICE._serialized_end = 1425
# @@protoc_insertion_point(module_scope)
