using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003192: Kyle
/// </summary>
public class _11003192 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0405160907008256$
    // - Heh heh heh...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0405160907008258$
                // - What brings you here?
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
