using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004326: Manager
/// </summary>
public class _11004326 : NpcScript {
    internal _11004326(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1010140307011506$ 
                // - Never thought I'd wind up in a place like this...
                return true;
            case 10:
                // $script:1010140307011507$ 
                // - Keep your distance, chump!
                // $script:1010140307011508$ 
                // - Hold on. You're one of those Sky Fortress people. Sorry, I thought you were another stalker.
                switch (selection) {
                    // $script:1010140307011509$
                    // - Why is $npcName:11004325[gender:0]$ here, anyway?
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:1010140307011510$ 
                // - About that... Come closer, okay? I don't want to exactly shout this out.
                // $script:1010140307011511$ 
                // - $npcName:11004325[gender:0]$ isn't so popular these days. He's getting a little old for the gig, and there's lots of hot young talent in the idol game.
                // $script:1010140307011512$ 
                // - Some stars are able to keep working into their old age. But these stars can compose and write their own songs. $npcName:11004325[gender:0]$ can't do neither.
                // $script:1010140307011513$ 
                // - But my boy here heard about this strange new land and thought he might take a vacation to find his muse.
                // $script:1010140307011514$ 
                // - He wouldn't take no for an answer. Lucky for us, the president of his fan club has an in with Sky Fortress and we were able to hitch a ride.
                switch (selection) {
                    // $script:1010140307011515$
                    // - Who's this fan club president?
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 30:
                // $script:1010140307011516$ 
                // - I can't exactly say. Confidentiality, you see. But between you and me, she's pretty high up in the Sky Fortress food chain, if you catch my drift.
                return true;
            default:
                return true;
        }
    }
}
