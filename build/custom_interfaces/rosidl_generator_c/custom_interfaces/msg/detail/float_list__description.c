// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from custom_interfaces:msg/FloatList.idl
// generated code does not contain a copyright notice

#include "custom_interfaces/msg/detail/float_list__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_custom_interfaces
const rosidl_type_hash_t *
custom_interfaces__msg__FloatList__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xc1, 0x1a, 0xf7, 0x20, 0xc9, 0x53, 0xb0, 0x9e,
      0x2b, 0xf3, 0x9d, 0xf7, 0x36, 0x0c, 0x9b, 0x9c,
      0x2c, 0xb6, 0xe1, 0xad, 0x41, 0x7f, 0xcd, 0xfe,
      0x42, 0xa8, 0xde, 0xb5, 0x44, 0x26, 0xa1, 0x8f,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char custom_interfaces__msg__FloatList__TYPE_NAME[] = "custom_interfaces/msg/FloatList";

// Define type names, field names, and default values
static char custom_interfaces__msg__FloatList__FIELD_NAME__data[] = "data";

static rosidl_runtime_c__type_description__Field custom_interfaces__msg__FloatList__FIELDS[] = {
  {
    {custom_interfaces__msg__FloatList__FIELD_NAME__data, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT_UNBOUNDED_SEQUENCE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
custom_interfaces__msg__FloatList__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {custom_interfaces__msg__FloatList__TYPE_NAME, 31, 31},
      {custom_interfaces__msg__FloatList__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float32[] data";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
custom_interfaces__msg__FloatList__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {custom_interfaces__msg__FloatList__TYPE_NAME, 31, 31},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 15, 15},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
custom_interfaces__msg__FloatList__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *custom_interfaces__msg__FloatList__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
