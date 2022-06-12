using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001332: Armachio
/// </summary>
public class _11001332 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217012607005248$
    // - Ugh...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217012607005251$
                // - Those knuckleheads! Why do they have to fight in here? They'll scare away the customers!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
