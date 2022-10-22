using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000994: Lotachi
/// </summary>
public class _11000994 : NpcScript {
    protected override int First() {
        // TODO: Job 1
        // TODO: RandomPick 40;50;60
    }

    // Select 0:
    // $script:0831180610001119$
    // - Ahoy! 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180610001120$
                // - Civilian ships are prohibited from sailing the waters around $map:02000183$. But for the low, low price of <font color="#ffd200">4,000</font> mesos, I can smuggle you into the area. Do you want to cast off now?
                return -1;
            case (40, 0):
                // $script:0831180610001124$
                // - Buddy, you need something?
                switch (selection) {
                    // $script:0831180610001125$
                    // - I want to go to $map:02000183$.
                    case 0:
                        return 41;
                    // $script:0831180610001126$
                    // - No.
                    case 1:
                        return 42;
                }
                return -1;
            case (41, 0):
                // $script:0831180610001127$
                // - $map:02000183$? Sorry, no can do. Civilian ships are prohibited from sailing in those waters.
                return -1;
            case (42, 0):
                // $script:0831180610001128$
                // - Alright then. I pretty much run the harbor, so if you need anything I can help you out. For a fee, of course.
                return -1;
            case (50, 0):
                // $script:0831180610001129$
                // - You want to go to $map:02000183$.
                //   The only way by ship is to pay someone to smuggle you in, and that costs at least <font color="#ffd200">4,000 mesos</font>. Bring the money, will you?
                return -1;
            case (60, 0):
                // $script:1209001710001308$
                // - Ugh, my throat... it feels like my last coughing fit tore it up. Ow... were you saying something?
                switch (selection) {
                    // $script:1209001710001309$
                    // - I want to get on the same ship as <font color="#ffd200">Bomar</font>.
                    case 0:
                        return 61;
                }
                return -1;
            case (61, 0):
                // $script:1209001710001310$
                // - All civilian ships are prohibited from sailing in that direction. Just a moment, I feel a cough coming on... no, false alarm. Okay, as I was saying, civilians are banned, but... if you really want to go, I could smuggle you in for a price—Hnrghh! Hurrgh! Ow, the cough's back... Hnrrgh! Hnrgh! Ahem! You see, I'm a master smuggler—hrrgh! Hurgh! Oh, who am I kidding? I can't sound like a smooth criminal with this cough. Look, it'll be 4,000 mesos to take you there. Please just pretend I said that with some gravitas.
                switch (selection) {
                    // $script:1210013910001316$
                    // - Don't worry, I'll get you what you need to wet your whistle.
                    case 0:
                        // TODO: goto 62
                        // TODO: gotoFail 63
                        return 63;
                }
                return -1;
            case (62, 0):
                // $script:1209001710001311$
                // - How about I—Hnrgh! Hnrgh!—let you on the ship in exchange for a glass of $item:20000087$? My cough's so bad I care more about that than money. That's an option if you don't want to—Hnrrgh! Hnrgh!—go to $map:2000183$ right away.
                switch (selection) {
                    // $script:1210233210001317$
                    // - Can you please send me there now?
                    case 0:
                        return 64;
                }
                return -1;
            case (64, 0):
                // functionID=1 
                // $script:1210233210001318$
                // - Okay. Argh, I can feel another coughing fit coming on! Leave me before you catch something!
                return -1;
            case (63, 0):
                // $script:1209001710001313$
                // - Thank you... I'd like a—Hnrgh! Hnrgh!—glass of $item:20000087$, please. $npcName:11000445[gender:1]$ mixes wonderful drinks over there on the beach. Hnrghh! Huuurrgh! 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            (42, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (61, 0) => NpcTalkButton.SelectableDistractor,
            (62, 0) => NpcTalkButton.SelectableDistractor,
            (64, 0) => NpcTalkButton.Close,
            (63, 0) => NpcTalkButton.Close,
            (1, 0) => NpcTalkButton.TakeBoat,
            _ => NpcTalkButton.None,
        };
    }
}
