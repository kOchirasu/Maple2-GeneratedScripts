using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000994: Lotachi
/// </summary>
public class _11000994 : NpcScript {
    internal _11000994(INpcScriptContext context) : base(context) {
        // TODO: Job 1
        // TODO: RandomPick 40;50;60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610001119$ 
                // - Ahoy! 
                return true;
            case 1:
                // $script:0831180610001120$ 
                // - Civilian ships are prohibited from sailing the waters around $map:02000183$. But for the low, low price of <font color="#ffd200">4,000</font> mesos, I can smuggle you into the area. Do you want to cast off now?
                return true;
            case 40:
                // $script:0831180610001124$ 
                // - Buddy, you need something?
                switch (selection) {
                    // $script:0831180610001125$
                    // - I want to go to $map:02000183$.
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0831180610001126$
                    // - No.
                    case 1:
                        Id = 42;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180610001127$ 
                // - $map:02000183$? Sorry, no can do. Civilian ships are prohibited from sailing in those waters.
                return true;
            case 42:
                // $script:0831180610001128$ 
                // - Alright then. I pretty much run the harbor, so if you need anything I can help you out. For a fee, of course.
                return true;
            case 50:
                // $script:0831180610001129$ 
                // - You want to go to $map:02000183$.
                //   The only way by ship is to pay someone to smuggle you in, and that costs at least <font color="#ffd200">4,000 mesos</font>. Bring the money, will you?
                return true;
            case 60:
                // $script:1209001710001308$ 
                // - Ugh, my throat... it feels like my last coughing fit tore it up. Ow... were you saying something?
                switch (selection) {
                    // $script:1209001710001309$
                    // - I want to get on the same ship as <font color="#ffd200">Bomar</font>.
                    case 0:
                        Id = 61;
                        return false;
                }
                return true;
            case 61:
                // $script:1209001710001310$ 
                // - All civilian ships are prohibited from sailing in that direction. Just a moment, I feel a cough coming on... no, false alarm. Okay, as I was saying, civilians are banned, but... if you really want to go, I could smuggle you in for a price—Hnrghh! Hurrgh! Ow, the cough's back... Hnrrgh! Hnrgh! Ahem! You see, I'm a master smuggler—hrrgh! Hurgh! Oh, who am I kidding? I can't sound like a smooth criminal with this cough. Look, it'll be 4,000 mesos to take you there. Please just pretend I said that with some gravitas.
                switch (selection) {
                    // $script:1210013910001316$
                    // - Don't worry, I'll get you what you need to wet your whistle.
                    case 0:
                        Id = 0; // TODO: 62 | 63
                        return false;
                }
                return true;
            case 62:
                // $script:1209001710001311$ 
                // - How about I—Hnrgh! Hnrgh!—let you on the ship in exchange for a glass of $item:20000087$? My cough's so bad I care more about that than money. That's an option if you don't want to—Hnrrgh! Hnrgh!—go to $map:2000183$ right away.
                switch (selection) {
                    // $script:1210233210001317$
                    // - Can you please send me there now?
                    case 0:
                        Id = 64;
                        return false;
                }
                return true;
            case 64:
                // $script:1210233210001318$ functionID=1 
                // - Okay. Argh, I can feel another coughing fit coming on! Leave me before you catch something!
                return true;
            case 63:
                // $script:1209001710001313$ 
                // - Thank you... I'd like a—Hnrgh! Hnrgh!—glass of $item:20000087$, please. $npcName:11000445[gender:1]$ mixes wonderful drinks over there on the beach. Hnrghh! Huuurrgh! 
                return true;
            default:
                return true;
        }
    }
}
