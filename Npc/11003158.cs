using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003158: Carly
/// </summary>
public class _11003158 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0306155707008054$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0306155707008058$
                // - This is my favorite place. It's beautiful and smells even better. And, you might not know this, but I can also eat delicious food here!
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
