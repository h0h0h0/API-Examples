=begin
#MINDBODY Public API

#No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

OpenAPI spec version: v6

Generated by: https://github.com/swagger-api/swagger-codegen.git
Swagger Codegen version: 2.4.6

=end

require 'date'

module SwaggerClient
  class AddAppointmentRequest
    # When `true`, indicates that a payment should be applied to the appointment.   <br />Default: **true**
    attr_accessor :apply_payment

    # The RRSID of the client for whom the new appointment is being made.
    attr_accessor :client_id

    # The duration of the appointment. This parameter is used to change the default duration of an appointment.
    attr_accessor :duration

    # The action taken to add this appointment.
    attr_accessor :execute

    # The end date and time of the new appointment. <br />  Default: **StartDateTime**, offset by the staff member’s default appointment duration.
    attr_accessor :end_date_time

    # The client’s service provider gender preference.
    attr_accessor :gender_preference

    # The ID of the location where the new appointment is to take place.
    attr_accessor :location_id

    # Any general notes about this appointment.
    attr_accessor :notes

    # If a user has Complementary and Alternative Medicine features enabled, this parameter assigns a provider ID to the appointment.
    attr_accessor :provider_id

    # A list of resource IDs to associate with the new appointment.
    attr_accessor :resource_ids

    #  Whether to send client an email for cancellations. An email is sent only if the client has an email address and automatic emails have been set up.   <br />Default: **false**
    attr_accessor :send_email

    # The session type associated with the new appointment.
    attr_accessor :session_type_id

    # The ID of the staff member who is adding the new appointment.
    attr_accessor :staff_id

    # When `true`, indicates that the staff member was requested specifically by the client.
    attr_accessor :staff_requested

    # The start date and time of the new appointment.
    attr_accessor :start_date_time

    #  When true, indicates that the method is to be validated, but no new appointment data is added.   <br />Default: **false**
    attr_accessor :test

    class EnumAttributeValidator
      attr_reader :datatype
      attr_reader :allowable_values

      def initialize(datatype, allowable_values)
        @allowable_values = allowable_values.map do |value|
          case datatype.to_s
          when /Integer/i
            value.to_i
          when /Float/i
            value.to_f
          else
            value
          end
        end
      end

      def valid?(value)
        !value || allowable_values.include?(value)
      end
    end

    # Attribute mapping from ruby-style variable name to JSON key.
    def self.attribute_map
      {
        :'apply_payment' => :'ApplyPayment',
        :'client_id' => :'ClientId',
        :'duration' => :'Duration',
        :'execute' => :'Execute',
        :'end_date_time' => :'EndDateTime',
        :'gender_preference' => :'GenderPreference',
        :'location_id' => :'LocationId',
        :'notes' => :'Notes',
        :'provider_id' => :'ProviderId',
        :'resource_ids' => :'ResourceIds',
        :'send_email' => :'SendEmail',
        :'session_type_id' => :'SessionTypeId',
        :'staff_id' => :'StaffId',
        :'staff_requested' => :'StaffRequested',
        :'start_date_time' => :'StartDateTime',
        :'test' => :'Test'
      }
    end

    # Attribute type mapping.
    def self.swagger_types
      {
        :'apply_payment' => :'BOOLEAN',
        :'client_id' => :'String',
        :'duration' => :'Integer',
        :'execute' => :'String',
        :'end_date_time' => :'DateTime',
        :'gender_preference' => :'String',
        :'location_id' => :'Integer',
        :'notes' => :'String',
        :'provider_id' => :'String',
        :'resource_ids' => :'Array<Integer>',
        :'send_email' => :'BOOLEAN',
        :'session_type_id' => :'Integer',
        :'staff_id' => :'Integer',
        :'staff_requested' => :'BOOLEAN',
        :'start_date_time' => :'DateTime',
        :'test' => :'BOOLEAN'
      }
    end

    # Initializes the object
    # @param [Hash] attributes Model attributes in the form of hash
    def initialize(attributes = {})
      return unless attributes.is_a?(Hash)

      # convert string to symbol for hash key
      attributes = attributes.each_with_object({}) { |(k, v), h| h[k.to_sym] = v }

      if attributes.has_key?(:'ApplyPayment')
        self.apply_payment = attributes[:'ApplyPayment']
      end

      if attributes.has_key?(:'ClientId')
        self.client_id = attributes[:'ClientId']
      end

      if attributes.has_key?(:'Duration')
        self.duration = attributes[:'Duration']
      end

      if attributes.has_key?(:'Execute')
        self.execute = attributes[:'Execute']
      end

      if attributes.has_key?(:'EndDateTime')
        self.end_date_time = attributes[:'EndDateTime']
      end

      if attributes.has_key?(:'GenderPreference')
        self.gender_preference = attributes[:'GenderPreference']
      end

      if attributes.has_key?(:'LocationId')
        self.location_id = attributes[:'LocationId']
      end

      if attributes.has_key?(:'Notes')
        self.notes = attributes[:'Notes']
      end

      if attributes.has_key?(:'ProviderId')
        self.provider_id = attributes[:'ProviderId']
      end

      if attributes.has_key?(:'ResourceIds')
        if (value = attributes[:'ResourceIds']).is_a?(Array)
          self.resource_ids = value
        end
      end

      if attributes.has_key?(:'SendEmail')
        self.send_email = attributes[:'SendEmail']
      end

      if attributes.has_key?(:'SessionTypeId')
        self.session_type_id = attributes[:'SessionTypeId']
      end

      if attributes.has_key?(:'StaffId')
        self.staff_id = attributes[:'StaffId']
      end

      if attributes.has_key?(:'StaffRequested')
        self.staff_requested = attributes[:'StaffRequested']
      end

      if attributes.has_key?(:'StartDateTime')
        self.start_date_time = attributes[:'StartDateTime']
      end

      if attributes.has_key?(:'Test')
        self.test = attributes[:'Test']
      end
    end

    # Show invalid properties with the reasons. Usually used together with valid?
    # @return Array for valid properties with the reasons
    def list_invalid_properties
      invalid_properties = Array.new
      if @client_id.nil?
        invalid_properties.push('invalid value for "client_id", client_id cannot be nil.')
      end

      if @location_id.nil?
        invalid_properties.push('invalid value for "location_id", location_id cannot be nil.')
      end

      if @session_type_id.nil?
        invalid_properties.push('invalid value for "session_type_id", session_type_id cannot be nil.')
      end

      if @staff_id.nil?
        invalid_properties.push('invalid value for "staff_id", staff_id cannot be nil.')
      end

      if @start_date_time.nil?
        invalid_properties.push('invalid value for "start_date_time", start_date_time cannot be nil.')
      end

      invalid_properties
    end

    # Check to see if the all the properties in the model are valid
    # @return true if the model is valid
    def valid?
      return false if @client_id.nil?
      gender_preference_validator = EnumAttributeValidator.new('String', ['None', 'Female', 'Male'])
      return false unless gender_preference_validator.valid?(@gender_preference)
      return false if @location_id.nil?
      return false if @session_type_id.nil?
      return false if @staff_id.nil?
      return false if @start_date_time.nil?
      true
    end

    # Custom attribute writer method checking allowed values (enum).
    # @param [Object] gender_preference Object to be assigned
    def gender_preference=(gender_preference)
      validator = EnumAttributeValidator.new('String', ['None', 'Female', 'Male'])
      unless validator.valid?(gender_preference)
        fail ArgumentError, 'invalid value for "gender_preference", must be one of #{validator.allowable_values}.'
      end
      @gender_preference = gender_preference
    end

    # Checks equality by comparing each attribute.
    # @param [Object] Object to be compared
    def ==(o)
      return true if self.equal?(o)
      self.class == o.class &&
          apply_payment == o.apply_payment &&
          client_id == o.client_id &&
          duration == o.duration &&
          execute == o.execute &&
          end_date_time == o.end_date_time &&
          gender_preference == o.gender_preference &&
          location_id == o.location_id &&
          notes == o.notes &&
          provider_id == o.provider_id &&
          resource_ids == o.resource_ids &&
          send_email == o.send_email &&
          session_type_id == o.session_type_id &&
          staff_id == o.staff_id &&
          staff_requested == o.staff_requested &&
          start_date_time == o.start_date_time &&
          test == o.test
    end

    # @see the `==` method
    # @param [Object] Object to be compared
    def eql?(o)
      self == o
    end

    # Calculates hash code according to all attributes.
    # @return [Fixnum] Hash code
    def hash
      [apply_payment, client_id, duration, execute, end_date_time, gender_preference, location_id, notes, provider_id, resource_ids, send_email, session_type_id, staff_id, staff_requested, start_date_time, test].hash
    end

    # Builds the object from hash
    # @param [Hash] attributes Model attributes in the form of hash
    # @return [Object] Returns the model itself
    def build_from_hash(attributes)
      return nil unless attributes.is_a?(Hash)
      self.class.swagger_types.each_pair do |key, type|
        if type =~ /\AArray<(.*)>/i
          # check to ensure the input is an array given that the the attribute
          # is documented as an array but the input is not
          if attributes[self.class.attribute_map[key]].is_a?(Array)
            self.send("#{key}=", attributes[self.class.attribute_map[key]].map { |v| _deserialize($1, v) })
          end
        elsif !attributes[self.class.attribute_map[key]].nil?
          self.send("#{key}=", _deserialize(type, attributes[self.class.attribute_map[key]]))
        end # or else data not found in attributes(hash), not an issue as the data can be optional
      end

      self
    end

    # Deserializes the data based on type
    # @param string type Data type
    # @param string value Value to be deserialized
    # @return [Object] Deserialized data
    def _deserialize(type, value)
      case type.to_sym
      when :DateTime
        DateTime.parse(value)
      when :Date
        Date.parse(value)
      when :String
        value.to_s
      when :Integer
        value.to_i
      when :Float
        value.to_f
      when :BOOLEAN
        if value.to_s =~ /\A(true|t|yes|y|1)\z/i
          true
        else
          false
        end
      when :Object
        # generic object (usually a Hash), return directly
        value
      when /\AArray<(?<inner_type>.+)>\z/
        inner_type = Regexp.last_match[:inner_type]
        value.map { |v| _deserialize(inner_type, v) }
      when /\AHash<(?<k_type>.+?), (?<v_type>.+)>\z/
        k_type = Regexp.last_match[:k_type]
        v_type = Regexp.last_match[:v_type]
        {}.tap do |hash|
          value.each do |k, v|
            hash[_deserialize(k_type, k)] = _deserialize(v_type, v)
          end
        end
      else # model
        temp_model = SwaggerClient.const_get(type).new
        temp_model.build_from_hash(value)
      end
    end

    # Returns the string representation of the object
    # @return [String] String presentation of the object
    def to_s
      to_hash.to_s
    end

    # to_body is an alias to to_hash (backward compatibility)
    # @return [Hash] Returns the object in the form of hash
    def to_body
      to_hash
    end

    # Returns the object in the form of hash
    # @return [Hash] Returns the object in the form of hash
    def to_hash
      hash = {}
      self.class.attribute_map.each_pair do |attr, param|
        value = self.send(attr)
        next if value.nil?
        hash[param] = _to_hash(value)
      end
      hash
    end

    # Outputs non-array value in the form of hash
    # For object, use to_hash. Otherwise, just return the value
    # @param [Object] value Any valid value
    # @return [Hash] Returns the value in the form of hash
    def _to_hash(value)
      if value.is_a?(Array)
        value.compact.map { |v| _to_hash(v) }
      elsif value.is_a?(Hash)
        {}.tap do |hash|
          value.each { |k, v| hash[k] = _to_hash(v) }
        end
      elsif value.respond_to? :to_hash
        value.to_hash
      else
        value
      end
    end
  end
end