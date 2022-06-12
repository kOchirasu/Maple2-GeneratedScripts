using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004327: Rolling Thunder
/// </summary>
public class _11004327 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1010140307011517$
    // - Hm...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1010140307011518$
                // - This place is... strange.
                switch (selection) {
                    // $script:1010140307011519$
                    // - I didn't expect to see you here.
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:1010140307011520$
                // - Hey! Didn't see you there. I'm here to represent $map:02000051$.
                switch (selection) {
                    // $script:1010140307011521$
                    // - Couldn't you have sent a diplomat?
                    case 0:
                        return 30;
                }
                return -1;
            case (30, 0):
                // $script:1010140307011522$
                // - ...There were things I had to see for myself.
                return 30;
            case (30, 1):
                // $script:1010140307011523$
                // - My father appeared to me in a dream. He said that $map:02000051$ would soon face a grave danger...
                return 30;
            case (30, 2):
                // $script:1010140307011524$
                // - And then this place showed up. It couldn't be a coincidence, right?
                return 30;
            case (30, 3):
                // $script:1010140307011525$
                // - More importantly, $npcName:11004328[gender:1]$ has a bad feeling about all this, and I trust her instincts.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Next,
            (30, 2) => NpcTalkButton.Next,
            (30, 3) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
