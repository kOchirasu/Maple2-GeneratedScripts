using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001068: Gaden
/// </summary>
public class _11001068 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003639$
    // - Hello.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003642$
                // - Did you come to enjoy Oil and Water's concert? Head up to the front of the stage if you did.
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
