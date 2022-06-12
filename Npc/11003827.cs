using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003827: Mason
/// </summary>
public class _11003827 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0115140307009751$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0115140307009752$
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
