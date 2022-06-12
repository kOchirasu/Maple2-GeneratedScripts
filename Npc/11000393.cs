using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000393: Buffett
/// </summary>
public class _11000393 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407001596$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407001599$
                // - When my manager is angry, he screams at the top of his lungs and throws anything he can get his hands on. No one can stop him. All you can do is avoid him.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
