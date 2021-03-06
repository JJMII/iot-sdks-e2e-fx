/**
 * IoT SDK Device & Client REST API
 * REST API definition for End-to-end testing of the Azure IoT SDKs.  All SDK APIs that are tested by our E2E tests need to be defined in this file.  This file takes some liberties with the API definitions.  In particular, response schemas are undefined, and error responses are also undefined.
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator 2.3.1.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

/*
 * DeviceApi.h
 *
 * 
 */

#ifndef DeviceApi_H_
#define DeviceApi_H_


#include <memory>
#include <corvusoft/restbed/session.hpp>
#include <corvusoft/restbed/resource.hpp>
#include <corvusoft/restbed/service.hpp>
#include <string>

namespace io {
namespace swagger {
namespace server {
namespace api {

class  DeviceApi: public virtual restbed::Service
{
public:
	DeviceApi();
	~DeviceApi();
	void startService(int const& port);
	void stopService();
};


/// <summary>
/// Connect to the azure IoT Hub as a device
/// </summary>
/// <remarks>
/// 
/// </remarks>
class  DeviceApiDeviceConnectTransportTypeResource: public restbed::Resource
{
public:
	DeviceApiDeviceConnectTransportTypeResource();
    virtual ~DeviceApiDeviceConnectTransportTypeResource();
    void PUT_method_handler(const std::shared_ptr<restbed::Session> session);
};

/// <summary>
/// Disconnect the device
/// </summary>
/// <remarks>
/// Disconnects from Azure IoTHub service.  More specifically, closes all connections and cleans up all resources for the active connection
/// </remarks>
class  DeviceApiDeviceConnectionIdDisconnectResource: public restbed::Resource
{
public:
	DeviceApiDeviceConnectionIdDisconnectResource();
    virtual ~DeviceApiDeviceConnectionIdDisconnectResource();
    void PUT_method_handler(const std::shared_ptr<restbed::Session> session);
};

/// <summary>
/// Enable methods
/// </summary>
/// <remarks>
/// 
/// </remarks>
class  DeviceApiDeviceConnectionIdEnableMethodsResource: public restbed::Resource
{
public:
	DeviceApiDeviceConnectionIdEnableMethodsResource();
    virtual ~DeviceApiDeviceConnectionIdEnableMethodsResource();
    void PUT_method_handler(const std::shared_ptr<restbed::Session> session);
};

/// <summary>
/// Wait for a method call, verify the request, and return the response.
/// </summary>
/// <remarks>
/// This is a workaround to deal with SDKs that only have method call operations that are sync.  This function responds to the method with the payload of this function, and then returns the method parameters.  Real-world implemenatations would never do this, but this is the only same way to write our test code right now (because the method handlers for C, Java, and probably Python all return the method response instead of supporting an async method call)
/// </remarks>
class  DeviceApiDeviceConnectionIdRoundtripMethodCallMethodNameResource: public restbed::Resource
{
public:
	DeviceApiDeviceConnectionIdRoundtripMethodCallMethodNameResource();
    virtual ~DeviceApiDeviceConnectionIdRoundtripMethodCallMethodNameResource();
    void PUT_method_handler(const std::shared_ptr<restbed::Session> session);
};


}
}
}
}

#endif /* DeviceApi_H_ */

