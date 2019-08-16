=begin
#MINDBODY Public API

#No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

OpenAPI spec version: v6

Generated by: https://github.com/swagger-api/swagger-codegen.git
Swagger Codegen version: 2.4.6

=end

require 'date'

module SwaggerClient
  class Location
    # A list of URLs of any images associated with this location.
    attr_accessor :additional_image_ur_ls

    # The first line of the location’s street address.
    attr_accessor :address

    # A second address line for the location’s street address, if needed.
    attr_accessor :address2

    # A list of strings representing amenities available at the location.
    attr_accessor :amenities

    # The business description for the location, as configured by the business owner.
    attr_accessor :business_description

    # The location’s city.
    attr_accessor :city

    # A description of the location.
    attr_accessor :description

    # When `true`, indicates that classes are held at this location.<br />  When `false`, Indicates that classes are not held at this location.
    attr_accessor :has_classes

    # The ID assigned to this location.
    attr_accessor :id

    # The location’s latitude.
    attr_accessor :latitude

    # The location’s longitude.
    attr_accessor :longitude

    # The name of this location.
    attr_accessor :name

    # The location’s phone number.
    attr_accessor :phone

    # The location’s phone extension.
    attr_accessor :phone_extension

    # The location’s postal code.
    attr_accessor :postal_code

    # The ID number assigned to this location.
    attr_accessor :site_id

    # The location’s state or province code.
    attr_accessor :state_prov_code

    # A decimal representation of the location’s first tax rate. Tax properties are provided to apply all taxes to the purchase price that the purchase is subject to. Use as many tax properties as needed to represent all the taxes that apply in the location. Enter a decimal number that represents the appropriate tax rate. For example, for an 8% sales tax, enter 0.08.
    attr_accessor :tax1

    # A decimal representation of the location’s second tax rate. See the example in the description of Tax1.
    attr_accessor :tax2

    # A decimal representation of the location’s third tax rate. See the example in the description of Tax1.
    attr_accessor :tax3

    # A decimal representation of the location’s fourth tax rate. See the example in the description of Tax1.
    attr_accessor :tax4

    # A decimal representation of the location’s fifth tax rate. See the example in the description of Tax1.
    attr_accessor :tax5

    # The number of reviews that clients have left for this location.
    attr_accessor :total_number_of_ratings

    # The average rating for the location, out of five stars.
    attr_accessor :average_rating

    # The number of distinct introductory pricing options available for purchase at this location.
    attr_accessor :total_number_of_deals

    # Attribute mapping from ruby-style variable name to JSON key.
    def self.attribute_map
      {
        :'additional_image_ur_ls' => :'AdditionalImageURLs',
        :'address' => :'Address',
        :'address2' => :'Address2',
        :'amenities' => :'Amenities',
        :'business_description' => :'BusinessDescription',
        :'city' => :'City',
        :'description' => :'Description',
        :'has_classes' => :'HasClasses',
        :'id' => :'Id',
        :'latitude' => :'Latitude',
        :'longitude' => :'Longitude',
        :'name' => :'Name',
        :'phone' => :'Phone',
        :'phone_extension' => :'PhoneExtension',
        :'postal_code' => :'PostalCode',
        :'site_id' => :'SiteID',
        :'state_prov_code' => :'StateProvCode',
        :'tax1' => :'Tax1',
        :'tax2' => :'Tax2',
        :'tax3' => :'Tax3',
        :'tax4' => :'Tax4',
        :'tax5' => :'Tax5',
        :'total_number_of_ratings' => :'TotalNumberOfRatings',
        :'average_rating' => :'AverageRating',
        :'total_number_of_deals' => :'TotalNumberOfDeals'
      }
    end

    # Attribute type mapping.
    def self.swagger_types
      {
        :'additional_image_ur_ls' => :'Array<String>',
        :'address' => :'String',
        :'address2' => :'String',
        :'amenities' => :'Array<Amenity>',
        :'business_description' => :'String',
        :'city' => :'String',
        :'description' => :'String',
        :'has_classes' => :'BOOLEAN',
        :'id' => :'Integer',
        :'latitude' => :'Float',
        :'longitude' => :'Float',
        :'name' => :'String',
        :'phone' => :'String',
        :'phone_extension' => :'String',
        :'postal_code' => :'String',
        :'site_id' => :'Integer',
        :'state_prov_code' => :'String',
        :'tax1' => :'Float',
        :'tax2' => :'Float',
        :'tax3' => :'Float',
        :'tax4' => :'Float',
        :'tax5' => :'Float',
        :'total_number_of_ratings' => :'Integer',
        :'average_rating' => :'Float',
        :'total_number_of_deals' => :'Integer'
      }
    end

    # Initializes the object
    # @param [Hash] attributes Model attributes in the form of hash
    def initialize(attributes = {})
      return unless attributes.is_a?(Hash)

      # convert string to symbol for hash key
      attributes = attributes.each_with_object({}) { |(k, v), h| h[k.to_sym] = v }

      if attributes.has_key?(:'AdditionalImageURLs')
        if (value = attributes[:'AdditionalImageURLs']).is_a?(Array)
          self.additional_image_ur_ls = value
        end
      end

      if attributes.has_key?(:'Address')
        self.address = attributes[:'Address']
      end

      if attributes.has_key?(:'Address2')
        self.address2 = attributes[:'Address2']
      end

      if attributes.has_key?(:'Amenities')
        if (value = attributes[:'Amenities']).is_a?(Array)
          self.amenities = value
        end
      end

      if attributes.has_key?(:'BusinessDescription')
        self.business_description = attributes[:'BusinessDescription']
      end

      if attributes.has_key?(:'City')
        self.city = attributes[:'City']
      end

      if attributes.has_key?(:'Description')
        self.description = attributes[:'Description']
      end

      if attributes.has_key?(:'HasClasses')
        self.has_classes = attributes[:'HasClasses']
      end

      if attributes.has_key?(:'Id')
        self.id = attributes[:'Id']
      end

      if attributes.has_key?(:'Latitude')
        self.latitude = attributes[:'Latitude']
      end

      if attributes.has_key?(:'Longitude')
        self.longitude = attributes[:'Longitude']
      end

      if attributes.has_key?(:'Name')
        self.name = attributes[:'Name']
      end

      if attributes.has_key?(:'Phone')
        self.phone = attributes[:'Phone']
      end

      if attributes.has_key?(:'PhoneExtension')
        self.phone_extension = attributes[:'PhoneExtension']
      end

      if attributes.has_key?(:'PostalCode')
        self.postal_code = attributes[:'PostalCode']
      end

      if attributes.has_key?(:'SiteID')
        self.site_id = attributes[:'SiteID']
      end

      if attributes.has_key?(:'StateProvCode')
        self.state_prov_code = attributes[:'StateProvCode']
      end

      if attributes.has_key?(:'Tax1')
        self.tax1 = attributes[:'Tax1']
      end

      if attributes.has_key?(:'Tax2')
        self.tax2 = attributes[:'Tax2']
      end

      if attributes.has_key?(:'Tax3')
        self.tax3 = attributes[:'Tax3']
      end

      if attributes.has_key?(:'Tax4')
        self.tax4 = attributes[:'Tax4']
      end

      if attributes.has_key?(:'Tax5')
        self.tax5 = attributes[:'Tax5']
      end

      if attributes.has_key?(:'TotalNumberOfRatings')
        self.total_number_of_ratings = attributes[:'TotalNumberOfRatings']
      end

      if attributes.has_key?(:'AverageRating')
        self.average_rating = attributes[:'AverageRating']
      end

      if attributes.has_key?(:'TotalNumberOfDeals')
        self.total_number_of_deals = attributes[:'TotalNumberOfDeals']
      end
    end

    # Show invalid properties with the reasons. Usually used together with valid?
    # @return Array for valid properties with the reasons
    def list_invalid_properties
      invalid_properties = Array.new
      invalid_properties
    end

    # Check to see if the all the properties in the model are valid
    # @return true if the model is valid
    def valid?
      true
    end

    # Checks equality by comparing each attribute.
    # @param [Object] Object to be compared
    def ==(o)
      return true if self.equal?(o)
      self.class == o.class &&
          additional_image_ur_ls == o.additional_image_ur_ls &&
          address == o.address &&
          address2 == o.address2 &&
          amenities == o.amenities &&
          business_description == o.business_description &&
          city == o.city &&
          description == o.description &&
          has_classes == o.has_classes &&
          id == o.id &&
          latitude == o.latitude &&
          longitude == o.longitude &&
          name == o.name &&
          phone == o.phone &&
          phone_extension == o.phone_extension &&
          postal_code == o.postal_code &&
          site_id == o.site_id &&
          state_prov_code == o.state_prov_code &&
          tax1 == o.tax1 &&
          tax2 == o.tax2 &&
          tax3 == o.tax3 &&
          tax4 == o.tax4 &&
          tax5 == o.tax5 &&
          total_number_of_ratings == o.total_number_of_ratings &&
          average_rating == o.average_rating &&
          total_number_of_deals == o.total_number_of_deals
    end

    # @see the `==` method
    # @param [Object] Object to be compared
    def eql?(o)
      self == o
    end

    # Calculates hash code according to all attributes.
    # @return [Fixnum] Hash code
    def hash
      [additional_image_ur_ls, address, address2, amenities, business_description, city, description, has_classes, id, latitude, longitude, name, phone, phone_extension, postal_code, site_id, state_prov_code, tax1, tax2, tax3, tax4, tax5, total_number_of_ratings, average_rating, total_number_of_deals].hash
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