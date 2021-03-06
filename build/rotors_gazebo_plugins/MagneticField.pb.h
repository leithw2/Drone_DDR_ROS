// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: MagneticField.proto

#ifndef PROTOBUF_MagneticField_2eproto__INCLUDED
#define PROTOBUF_MagneticField_2eproto__INCLUDED

#include <string>

#include <google/protobuf/stubs/common.h>

#if GOOGLE_PROTOBUF_VERSION < 3000000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please update
#error your headers.
#endif
#if 3000000 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/metadata.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/unknown_field_set.h>
#include "quaternion.pb.h"
#include "vector3d.pb.h"
#include "Header.pb.h"
// @@protoc_insertion_point(includes)

namespace gz_sensor_msgs {

// Internal implementation detail -- do not call these.
void protobuf_AddDesc_MagneticField_2eproto();
void protobuf_AssignDesc_MagneticField_2eproto();
void protobuf_ShutdownFile_MagneticField_2eproto();

class MagneticField;

// ===================================================================

class MagneticField : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:gz_sensor_msgs.MagneticField) */ {
 public:
  MagneticField();
  virtual ~MagneticField();

  MagneticField(const MagneticField& from);

  inline MagneticField& operator=(const MagneticField& from) {
    CopyFrom(from);
    return *this;
  }

  inline const ::google::protobuf::UnknownFieldSet& unknown_fields() const {
    return _internal_metadata_.unknown_fields();
  }

  inline ::google::protobuf::UnknownFieldSet* mutable_unknown_fields() {
    return _internal_metadata_.mutable_unknown_fields();
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const MagneticField& default_instance();

  void Swap(MagneticField* other);

  // implements Message ----------------------------------------------

  inline MagneticField* New() const { return New(NULL); }

  MagneticField* New(::google::protobuf::Arena* arena) const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const MagneticField& from);
  void MergeFrom(const MagneticField& from);
  void Clear();
  bool IsInitialized() const;

  int ByteSize() const;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input);
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* output) const;
  ::google::protobuf::uint8* SerializeWithCachedSizesToArray(::google::protobuf::uint8* output) const {
    return InternalSerializeWithCachedSizesToArray(false, output);
  }
  int GetCachedSize() const { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const;
  void InternalSwap(MagneticField* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return _internal_metadata_.arena();
  }
  inline void* MaybeArenaPtr() const {
    return _internal_metadata_.raw_arena_ptr();
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // required .gz_std_msgs.Header header = 1;
  bool has_header() const;
  void clear_header();
  static const int kHeaderFieldNumber = 1;
  const ::gz_std_msgs::Header& header() const;
  ::gz_std_msgs::Header* mutable_header();
  ::gz_std_msgs::Header* release_header();
  void set_allocated_header(::gz_std_msgs::Header* header);

  // required .gazebo.msgs.Vector3d magnetic_field = 2;
  bool has_magnetic_field() const;
  void clear_magnetic_field();
  static const int kMagneticFieldFieldNumber = 2;
  const ::gazebo::msgs::Vector3d& magnetic_field() const;
  ::gazebo::msgs::Vector3d* mutable_magnetic_field();
  ::gazebo::msgs::Vector3d* release_magnetic_field();
  void set_allocated_magnetic_field(::gazebo::msgs::Vector3d* magnetic_field);

  // repeated float magnetic_field_covariance = 3 [packed = true];
  int magnetic_field_covariance_size() const;
  void clear_magnetic_field_covariance();
  static const int kMagneticFieldCovarianceFieldNumber = 3;
  float magnetic_field_covariance(int index) const;
  void set_magnetic_field_covariance(int index, float value);
  void add_magnetic_field_covariance(float value);
  const ::google::protobuf::RepeatedField< float >&
      magnetic_field_covariance() const;
  ::google::protobuf::RepeatedField< float >*
      mutable_magnetic_field_covariance();

  // @@protoc_insertion_point(class_scope:gz_sensor_msgs.MagneticField)
 private:
  inline void set_has_header();
  inline void clear_has_header();
  inline void set_has_magnetic_field();
  inline void clear_has_magnetic_field();

  // helper for ByteSize()
  int RequiredFieldsByteSizeFallback() const;

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::google::protobuf::uint32 _has_bits_[1];
  mutable int _cached_size_;
  ::gz_std_msgs::Header* header_;
  ::gazebo::msgs::Vector3d* magnetic_field_;
  ::google::protobuf::RepeatedField< float > magnetic_field_covariance_;
  mutable int _magnetic_field_covariance_cached_byte_size_;
  friend void  protobuf_AddDesc_MagneticField_2eproto();
  friend void protobuf_AssignDesc_MagneticField_2eproto();
  friend void protobuf_ShutdownFile_MagneticField_2eproto();

  void InitAsDefaultInstance();
  static MagneticField* default_instance_;
};
// ===================================================================


// ===================================================================

#if !PROTOBUF_INLINE_NOT_IN_HEADERS
// MagneticField

// required .gz_std_msgs.Header header = 1;
inline bool MagneticField::has_header() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void MagneticField::set_has_header() {
  _has_bits_[0] |= 0x00000001u;
}
inline void MagneticField::clear_has_header() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void MagneticField::clear_header() {
  if (header_ != NULL) header_->::gz_std_msgs::Header::Clear();
  clear_has_header();
}
inline const ::gz_std_msgs::Header& MagneticField::header() const {
  // @@protoc_insertion_point(field_get:gz_sensor_msgs.MagneticField.header)
  return header_ != NULL ? *header_ : *default_instance_->header_;
}
inline ::gz_std_msgs::Header* MagneticField::mutable_header() {
  set_has_header();
  if (header_ == NULL) {
    header_ = new ::gz_std_msgs::Header;
  }
  // @@protoc_insertion_point(field_mutable:gz_sensor_msgs.MagneticField.header)
  return header_;
}
inline ::gz_std_msgs::Header* MagneticField::release_header() {
  // @@protoc_insertion_point(field_release:gz_sensor_msgs.MagneticField.header)
  clear_has_header();
  ::gz_std_msgs::Header* temp = header_;
  header_ = NULL;
  return temp;
}
inline void MagneticField::set_allocated_header(::gz_std_msgs::Header* header) {
  delete header_;
  header_ = header;
  if (header) {
    set_has_header();
  } else {
    clear_has_header();
  }
  // @@protoc_insertion_point(field_set_allocated:gz_sensor_msgs.MagneticField.header)
}

// required .gazebo.msgs.Vector3d magnetic_field = 2;
inline bool MagneticField::has_magnetic_field() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void MagneticField::set_has_magnetic_field() {
  _has_bits_[0] |= 0x00000002u;
}
inline void MagneticField::clear_has_magnetic_field() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void MagneticField::clear_magnetic_field() {
  if (magnetic_field_ != NULL) magnetic_field_->::gazebo::msgs::Vector3d::Clear();
  clear_has_magnetic_field();
}
inline const ::gazebo::msgs::Vector3d& MagneticField::magnetic_field() const {
  // @@protoc_insertion_point(field_get:gz_sensor_msgs.MagneticField.magnetic_field)
  return magnetic_field_ != NULL ? *magnetic_field_ : *default_instance_->magnetic_field_;
}
inline ::gazebo::msgs::Vector3d* MagneticField::mutable_magnetic_field() {
  set_has_magnetic_field();
  if (magnetic_field_ == NULL) {
    magnetic_field_ = new ::gazebo::msgs::Vector3d;
  }
  // @@protoc_insertion_point(field_mutable:gz_sensor_msgs.MagneticField.magnetic_field)
  return magnetic_field_;
}
inline ::gazebo::msgs::Vector3d* MagneticField::release_magnetic_field() {
  // @@protoc_insertion_point(field_release:gz_sensor_msgs.MagneticField.magnetic_field)
  clear_has_magnetic_field();
  ::gazebo::msgs::Vector3d* temp = magnetic_field_;
  magnetic_field_ = NULL;
  return temp;
}
inline void MagneticField::set_allocated_magnetic_field(::gazebo::msgs::Vector3d* magnetic_field) {
  delete magnetic_field_;
  magnetic_field_ = magnetic_field;
  if (magnetic_field) {
    set_has_magnetic_field();
  } else {
    clear_has_magnetic_field();
  }
  // @@protoc_insertion_point(field_set_allocated:gz_sensor_msgs.MagneticField.magnetic_field)
}

// repeated float magnetic_field_covariance = 3 [packed = true];
inline int MagneticField::magnetic_field_covariance_size() const {
  return magnetic_field_covariance_.size();
}
inline void MagneticField::clear_magnetic_field_covariance() {
  magnetic_field_covariance_.Clear();
}
inline float MagneticField::magnetic_field_covariance(int index) const {
  // @@protoc_insertion_point(field_get:gz_sensor_msgs.MagneticField.magnetic_field_covariance)
  return magnetic_field_covariance_.Get(index);
}
inline void MagneticField::set_magnetic_field_covariance(int index, float value) {
  magnetic_field_covariance_.Set(index, value);
  // @@protoc_insertion_point(field_set:gz_sensor_msgs.MagneticField.magnetic_field_covariance)
}
inline void MagneticField::add_magnetic_field_covariance(float value) {
  magnetic_field_covariance_.Add(value);
  // @@protoc_insertion_point(field_add:gz_sensor_msgs.MagneticField.magnetic_field_covariance)
}
inline const ::google::protobuf::RepeatedField< float >&
MagneticField::magnetic_field_covariance() const {
  // @@protoc_insertion_point(field_list:gz_sensor_msgs.MagneticField.magnetic_field_covariance)
  return magnetic_field_covariance_;
}
inline ::google::protobuf::RepeatedField< float >*
MagneticField::mutable_magnetic_field_covariance() {
  // @@protoc_insertion_point(field_mutable_list:gz_sensor_msgs.MagneticField.magnetic_field_covariance)
  return &magnetic_field_covariance_;
}

#endif  // !PROTOBUF_INLINE_NOT_IN_HEADERS

// @@protoc_insertion_point(namespace_scope)

}  // namespace gz_sensor_msgs

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_MagneticField_2eproto__INCLUDED
