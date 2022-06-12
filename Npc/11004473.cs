using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004473: Tenellus
/// </summary>
public class _11004473 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012145$
    // - Huh? Who're you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012146$
                // - Huh? Who're you?
                return 10;
            case (10, 1):
                // $script:1227192907012147$
                // - Wait, aren't you $MyPCName$? Wow! It really <i>is</i> you, in the flesh!
                switch (selection) {
                    // $script:1227192907012148$
                    // - Stop. You're making me blush.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012149$
                // - What, afraid of a little fame? How lame. This must be why they say you should never meet your heroes.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
