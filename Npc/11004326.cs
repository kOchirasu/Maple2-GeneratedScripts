using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004326: Manager
/// </summary>
public class _11004326 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1010140307011506$
    // - Never thought I'd wind up in a place like this...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1010140307011507$
                // - Keep your distance, chump!
                return 10;
            case (10, 1):
                // $script:1010140307011508$
                // - Hold on. You're one of those Sky Fortress people. Sorry, I thought you were another stalker.
                switch (selection) {
                    // $script:1010140307011509$
                    // - Why is $npcName:11004325[gender:0]$ here, anyway?
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:1010140307011510$
                // - About that... Come closer, okay? I don't want to exactly shout this out.
                return 20;
            case (20, 1):
                // $script:1010140307011511$
                // - $npcName:11004325[gender:0]$ isn't so popular these days. He's getting a little old for the gig, and there's lots of hot young talent in the idol game.
                return 20;
            case (20, 2):
                // $script:1010140307011512$
                // - Some stars are able to keep working into their old age. But these stars can compose and write their own songs. $npcName:11004325[gender:0]$ can't do neither.
                return 20;
            case (20, 3):
                // $script:1010140307011513$
                // - But my boy here heard about this strange new land and thought he might take a vacation to find his muse.
                return 20;
            case (20, 4):
                // $script:1010140307011514$
                // - He wouldn't take no for an answer. Lucky for us, the president of his fan club has an in with Sky Fortress and we were able to hitch a ride.
                switch (selection) {
                    // $script:1010140307011515$
                    // - Who's this fan club president?
                    case 0:
                        return 30;
                }
                return -1;
            case (30, 0):
                // $script:1010140307011516$
                // - I can't exactly say. Confidentiality, you see. But between you and me, she's pretty high up in the Sky Fortress food chain, if you catch my drift.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Next,
            (20, 2) => NpcTalkButton.Next,
            (20, 3) => NpcTalkButton.Next,
            (20, 4) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
