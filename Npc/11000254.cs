using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000254: Jane
/// </summary>
public class _11000254 : NpcScript {
    protected override int First() {
        return 60;
    }

    // Select 0:
    // $script:0831180407001056$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (60, 0):
                // $script:0831180407001060$
                // - Hey, there! If you've got a style in mind, we can make it happen. If you don't, maybe a magazine will inspire you. Want one?
                switch (selection) {
                    // $script:0831180407001061$
                    // - Yep.
                    case 0:
                        // TODO: goto 61,62
                        // TODO: gotoFail 63
                        return -1;
                    // $script:0831180407001062$
                    // - I'd like some advice.
                    case 1:
                        return 64;
                }
                return -1;
            case (61, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180407001063$
                // - Sure thing. This has all the latest styles. Have a seat and check them out.
                return -1;
            case (62, 0):
                // $script:0831180407001064$
                // - Err... I'm afraid you already have the only magazine we have. Sorry about that.
                return -1;
            case (63, 0):
                // $script:0831180407001065$
                // - Oh, friend... I'm afraid your bag is too heavy. Why don't you lighten it first?
                return -1;
            case (64, 0):
                // $script:0831180407001066$
                // - Sure! I love nothing more than helping match people with the hair of their dreams. Let's chat and find something that's totally you!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (61, 0) => NpcTalkButton.Close,
            (62, 0) => NpcTalkButton.Close,
            (63, 0) => NpcTalkButton.Close,
            (64, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
