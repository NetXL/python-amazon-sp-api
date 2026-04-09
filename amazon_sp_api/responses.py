from typing import Dict, List, Optional, Type

from amazon_sp_api.objects import Order, BuyerInfo, OrderItem, Address, InboundShipmentPlan


class SpApiResponse(object):
    def __init__(self, data: dict[str, any]):
        pass


class ListOrdersResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)
        payload = data.get('payload', {})
        self.orders: list[Order] = [Order(data=x) for x in payload.get('Orders', [])]


class GetOrderResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)
        self.order: Order = Order(data=data.get('payload', {}))


class GetOrderBuyerInfoResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)
        self.buyer_info: BuyerInfo = BuyerInfo(data=data.get('payload', {}))


class GetOrderItemsResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)
        payload = data.get('payload', {})
        self.items: list[OrderItem] = [OrderItem(data=x) for x in payload.get('OrderItems', [])]


class GetOrderAddressResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)
        payload = data.get('payload', {})
        self.address: Address = Address(data=payload.get('ShippingAddress', {}))


class ListSupplySourcesResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)


class CreateSupplySourcesResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)


class GetSubscriptionsResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)


class GetDestinationsResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)


class CreateDestinationResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)


class UpdateOrderStatusResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)


class RestrictedDataTokenResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)
        self.token = data.get('restrictedDataToken', None)


class GetEligibleShipmentServicesResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)
        payload = data.get('payload', {})
        self.shipping_service_list = payload.get('ShippingServiceList', [])


class CreateShipmentResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)
        for k, v in data.get('payload', {}).items():
            setattr(self, k, v)


class RequestReportResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)
        self.report_id = data.get('reportId', None)


class GetReportResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)
        self.report_id = data.get('reportId', None)
        self.processing_status = data.get('processingStatus', None)
        self.document_id = data.get('reportDocumentId', None)


class ReportDocumentResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)
        self.url = data.get('url', None)
        self.compression_algorithm = data.get('compressionAlgorithm', None)


class GetReportsResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)
        self.reports = data.get('reports', {})


class ConfirmShipmentResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)
        for k, v in data.get('payload', {}).items():
            setattr(self, k, v)


class CreateInboundShipmentPlanResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)
        self.plan_id = data.get('inboundPlanId')
        self.operation_id = data.get('operationId')

    @property
    def is_valid(self):
        return self.plan_id is not None and self.operation_id is not None

    @property
    def is_multiple_fulfilment_centers(self):
        return False


class GetListingItemResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)
        self.sku = data.get('sku')
        self.summaries = data.get('summaries', [])


class CreateInboundShipmentResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)
        for k, v in data.get('payload', {}).items():
            setattr(self, k, v)


class PatchListingResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)


class OperationStatusResponse(SpApiResponse):
    def __init__(self, data: dict[str, any]):
        super().__init__(data)
        self.status = data.get('operationStatus')
        self.operation_id = data.get('operationId')
        self.operation = data.get('operation')
        self.problems = []
        for problem in data.get('operationProblems'):
            self.problems.append(problem)
