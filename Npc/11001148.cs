using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001148: Danpa
/// </summary>
public class _11001148 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0915221607003971$
    // - What? If it's not urgent, come back later.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0915221607003974$
                // - See the fortress over there? It's got to be full of all kinds of amazing stuff worth collecting. Say, would you be interested in checking it out?
                switch (selection) {
                    // $script:0915221607003975$
                    // - I don't think there's much of value left in that abandoned fortress.
                    case 0:
                        return 31;
                    // $script:0915221607003976$
                    // - I'm a little more worried about the monsters guarding it.
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0915221607003977$
                // - <font color="#909090">(He chuckles.)</font>
                //   Well I do! It's gotta be chock full of treasure. I can tell, just by the look of it. I guess we'll see which of us is right.
                return -1;
            case (32, 0):
                // $script:0915221607003978$
                // - No kidding. Why do you think I haven't gone inside? I wish someone would take care of them for me...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
