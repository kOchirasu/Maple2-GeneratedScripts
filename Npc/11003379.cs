using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003379: Haster
/// </summary>
public class _11003379 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0613105907008550$
    // - ...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0613105907008551$
                // - Can't you find someone else to bother...?
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
