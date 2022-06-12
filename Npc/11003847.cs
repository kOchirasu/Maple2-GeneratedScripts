using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003847: Schatten
/// </summary>
public class _11003847 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0117175907009809$
    // - I am the shadow that evil fears.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0117175907009810$
                // - Hey there. Did you miss me?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
