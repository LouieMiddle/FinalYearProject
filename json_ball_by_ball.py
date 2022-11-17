from enum import Enum

from marshmallow_dataclass import dataclass
from marshmallow_enum import EnumField
from dataclass_wizard import json_field


@dataclass
class TwoDPosition:
    x: int
    y: int


@dataclass
class ThreeDPosition:
    x: int
    y: int
    z: int


@dataclass
class Trajectory:
    batStatPosition: TwoDPosition
    bounceAngle: float
    bouncePosition: ThreeDPosition
    cof: float
    cor: float
    creasePosition: ThreeDPosition
    deviation: float
    dropAngle: float
    impactPosition: ThreeDPosition
    initialAngle: float
    landingPosition: ThreeDPosition
    offBatAngle: int
    offBatSpeed: int
    pbr: float
    reactionTimeToCrease: float = json_field("reactionTime(to crease)")
    reactionTimeToInterception: float = json_field("reactionTime(to interception)")
    realDistance: int
    releasePosition: ThreeDPosition
    releaseSpeed: float
    spinRate: int
    stumpPosition: ThreeDPosition
    swing: float
    trajectoryData: str


@dataclass
class Batsman:
    id: str
    isRightHanded: bool
    name: str


@dataclass
class Bowler:
    id: str
    isRightHanded: bool
    name: str
    spell: int


@dataclass
class BattingTeam:
    batsman: Batsman
    batsmanPartner: Batsman
    home: bool
    id: str
    name: str


@dataclass
class DeliveryNumber:
    ball: int
    day: int
    innings: int
    over: int


@dataclass
class DeliveryType(Enum):
    SPIN = "Spin"
    SEAM = "Seam"


@dataclass
class Wicket:
    isWicket: bool


@dataclass
class ScoringInformation:
    extrasScore: int
    extrasType: str
    score: int
    wicket: Wicket


@dataclass
class ShotInformation:
    # TODO loop through files and get all strs for these and store as enum
    batsmanWeight: str
    shotAttacked: str
    shotPlayed: str
    shotTypeAdditional: str


@dataclass
class Delivery:
    deliveryNumber: DeliveryNumber
    deliveryType: EnumField(DeliveryType)
    isPavilionEnd: bool
    round: bool
    scoringInformation: ScoringInformation
    shotInformation: ShotInformation
    timecode: str
    trajectory: Trajectory


@dataclass
class BowlingTeam:
    bowler: Bowler
    bowlerPartner: Bowler
    home: bool
    name: str


@dataclass
class Match:
    battingTeam: BattingTeam
    bowlingTeam: BowlingTeam
    delivery: Delivery
    name: str


@dataclass
class BallByBall:
    country: str
    format: str
    international: bool
    match: Match
    tourName: str
