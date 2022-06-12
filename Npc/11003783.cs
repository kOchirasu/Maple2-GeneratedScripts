using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003783: Mason
/// </summary>
public class _11003783 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1213192607009636$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1213192607009637$
                // - There's work to be done.
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
