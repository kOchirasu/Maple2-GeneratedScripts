using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001732: Entrance Door
/// </summary>
public class _11001732 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0728022507006977$
    // - Accessing system. Confirming credentials...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0728024607006978$
                // - Security systems will be put online if you do not verify your credentials. Failure to connect will require you to re-verify your credentials at the front gate.
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
