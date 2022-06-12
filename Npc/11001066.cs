using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001066: Treno
/// </summary>
public class _11001066 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003630$
    // - Hello.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003633$
                // - Waiting for the $map:02000184$ tour train? We're sorry, but it won't be operating for a while.
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
