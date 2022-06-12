using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000473: Bunny Gal
/// </summary>
public class _11000473 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50
    }

    // Select 0:
    // $script:0831180407002069$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407002073$
                // - I don't recognize you. Is this your first time here?
                return -1;
            case (50, 0):
                // $script:0831180407002074$
                // - You've been staring at me. Interested?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
