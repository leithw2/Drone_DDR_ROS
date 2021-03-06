// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: PoseWithCovariance.proto

#ifndef PROTOBUF_PoseWithCovariance_2eproto__INCLUDED
#define PROTOBUF_PoseWithCovariance_2eproto__INCLUDED

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
#include "pose.pb.h"
// @@protoc_insertion_point(includes)

namespace gz_geometry_msgs {

// Internal implementation detail -- do not call these.
void protobuf_AddDesc_PoseWithCovariance_2eproto();
void protobuf_AssignDesc_PoseWithCovariance_2eproto();
void protobuf_ShutdownFile_PoseWithCovariance_2eproto();

class PoseWithCovariance;

// ===================================================================

class PoseWithCovariance : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:gz_geometry_msgs.PoseWithCovariance) */ {
 public:
  PoseWithCovariance();
  virtual ~PoseWithCovariance();

  PoseWithCovariance(const PoseWithCovariance& from);

  inline PoseWithCovariance& operator=(const PoseWithCovariance& from) {
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
  static const PoseWithCovariance& default_instance();

  void Swap(PoseWithCovariance* other);

  // implements Message ----------------------------------------------

  inline PoseWithCovariance* New() const { return New(NULL); }

  PoseWithCovariance* New(::google::protobuf::Arena* arena) const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const PoseWithCovariance& from);
  void MergeFrom(const PoseWithCovariance& from);
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
  void InternalSwap(PoseWithCovariance* other);
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

  // required .gazebo.msgs.Pose pose = 1;
  bool has_pose() const;
  void clear_pose();
  static const int kPoseFieldNumber = 1;
  const ::gazebo::msgs::Pose& pose() const;
  ::gazebo::msgs::Pose* mutable_pose();
  ::gazebo::msgs::Pose* release_pose();
  void set_allocated_pose(::gazebo::msgs::Pose* pose);

  // repeated double covariance = 2 [packed = true];
  int covariance_size() const;
  void clear_covariance();
  static const int kCovarianceFieldNumber = 2;
  double covariance(int index) const;
  void set_covariance(int index, double value);
  void add_covariance(double value);
  const ::google::protobuf::RepeatedField< double >&
      covariance() const;
  ::google::protobuf::RepeatedField< double >*
      mutable_covariance();

  // @@protoc_insertion_point(class_scope:gz_geometry_msgs.PoseWithCovariance)
 private:
  inline void set_has_pose();
  inline void clear_has_pose();

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::google::protobuf::uint32 _has_bits_[1];
  mutable int _cached_size_;
  ::gazebo::msgs::Pose* pose_;
  ::google::protobuf::RepeatedField< double > covariance_;
  mutable int _covariance_cached_byte_size_;
  friend void  protobuf_AddDesc_PoseWithCovariance_2eproto();
  friend void protobuf_AssignDesc_PoseWithCovariance_2eproto();
  friend void protobuf_ShutdownFile_PoseWithCovariance_2eproto();

  void InitAsDefaultInstance();
  static PoseWithCovariance* default_instance_;
};
// ===================================================================


// ===================================================================

#if !PROTOBUF_INLINE_NOT_IN_HEADERS
// PoseWithCovariance

// required .gazebo.msgs.Pose pose = 1;
inline bool PoseWithCovariance::has_pose() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void PoseWithCovariance::set_has_pose() {
  _has_bits_[0] |= 0x00000001u;
}
inline void PoseWithCovariance::clear_has_pose() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void PoseWithCovariance::clear_pose() {
  if (pose_ != NULL) pose_->::gazebo::msgs::Pose::Clear();
  clear_has_pose();
}
inline const ::gazebo::msgs::Pose& PoseWithCovariance::pose() const {
  // @@protoc_insertion_point(field_get:gz_geometry_msgs.PoseWithCovariance.pose)
  return pose_ != NULL ? *pose_ : *default_instance_->pose_;
}
inline ::gazebo::msgs::Pose* PoseWithCovariance::mutable_pose() {
  set_has_pose();
  if (pose_ == NULL) {
    pose_ = new ::gazebo::msgs::Pose;
  }
  // @@protoc_insertion_point(field_mutable:gz_geometry_msgs.PoseWithCovariance.pose)
  return pose_;
}
inline ::gazebo::msgs::Pose* PoseWithCovariance::release_pose() {
  // @@protoc_insertion_point(field_release:gz_geometry_msgs.PoseWithCovariance.pose)
  clear_has_pose();
  ::gazebo::msgs::Pose* temp = pose_;
  pose_ = NULL;
  return temp;
}
inline void PoseWithCovariance::set_allocated_pose(::gazebo::msgs::Pose* pose) {
  delete pose_;
  pose_ = pose;
  if (pose) {
    set_has_pose();
  } else {
    clear_has_pose();
  }
  // @@protoc_insertion_point(field_set_allocated:gz_geometry_msgs.PoseWithCovariance.pose)
}

// repeated double covariance = 2 [packed = true];
inline int PoseWithCovariance::covariance_size() const {
  return covariance_.size();
}
inline void PoseWithCovariance::clear_covariance() {
  covariance_.Clear();
}
inline double PoseWithCovariance::covariance(int index) const {
  // @@protoc_insertion_point(field_get:gz_geometry_msgs.PoseWithCovariance.covariance)
  return covariance_.Get(index);
}
inline void PoseWithCovariance::set_covariance(int index, double value) {
  covariance_.Set(index, value);
  // @@protoc_insertion_point(field_set:gz_geometry_msgs.PoseWithCovariance.covariance)
}
inline void PoseWithCovariance::add_covariance(double value) {
  covariance_.Add(value);
  // @@protoc_insertion_point(field_add:gz_geometry_msgs.PoseWithCovariance.covariance)
}
inline const ::google::protobuf::RepeatedField< double >&
PoseWithCovariance::covariance() const {
  // @@protoc_insertion_point(field_list:gz_geometry_msgs.PoseWithCovariance.covariance)
  return covariance_;
}
inline ::google::protobuf::RepeatedField< double >*
PoseWithCovariance::mutable_covariance() {
  // @@protoc_insertion_point(field_mutable_list:gz_geometry_msgs.PoseWithCovariance.covariance)
  return &covariance_;
}

#endif  // !PROTOBUF_INLINE_NOT_IN_HEADERS

// @@protoc_insertion_point(namespace_scope)

}  // namespace gz_geometry_msgs

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_PoseWithCovariance_2eproto__INCLUDED
