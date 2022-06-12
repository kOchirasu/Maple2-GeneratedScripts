using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004513: Mannstad Gunner
/// </summary>
public class _11004513 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1228182607012469$
    // - My bullets always hit their mark!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1228182607012470$
                // - My bullets always hit their mark!
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
