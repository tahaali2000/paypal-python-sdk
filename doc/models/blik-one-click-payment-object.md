
# BLIK One Click Payment Object

Information used to pay using BLIK one-click flow.

## Structure

`BLIKOneClickPaymentObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `consumer_reference` | `str` | Optional | The merchant generated, unique reference serving as a primary identifier for accounts connected between Blik and a merchant.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `64`, *Pattern*: `^[ -~]{3,64}$` |

## Example (as JSON)

```json
{
  "consumer_reference": "consumer_reference0"
}
```

