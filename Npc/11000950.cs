using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000950: Tomtam
/// </summary>
public class _11000950 : NpcScript {
    protected override int First() {
        // TODO: Job 1
        // TODO: RandomPick 10
    }

    // Select 0:
    // $script:0831180610001114$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180610001117$
                // - You look a right mess! How about I treat you? It'll only be a measly $paneltyPrice$ mesos.
                //   Don't worry, I'm a real doctor!
                return -1;
            case (10, 0):
                // $script:0831180610001118$
                // - You don't look like you need my help right now, but you will eventually. Oh yes, trust me on this one. Bad things happen around here all the time. 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (1, 0) => NpcTalkButton.PenaltyResolve,
            _ => NpcTalkButton.None,
        };
    }
}
