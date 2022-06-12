using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003203: Joddy
/// </summary>
public class _11003203 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0518141907008520$
    // - Training to be a guard is tough.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0518141907008521$
                // - Huh...? Who is this small friend?
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
