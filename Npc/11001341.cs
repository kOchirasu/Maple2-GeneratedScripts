using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001341: Donnie
/// </summary>
public class _11001341 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217012607005284$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217012607005287$
                // - Where are all these bugs coming from? They'll take over the skate park at this rate. Then Ludari City... and then, the world!
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
