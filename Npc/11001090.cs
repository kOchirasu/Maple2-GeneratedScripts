using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001090: 
/// </summary>
public class _11001090 : NpcScript {
    protected override void FirstScript() {
        // TODO: Job 1
        // (Id, Button) = (1, NpcTalkButton.Close);
        // TODO: RandomPick 10
        // (Id, Button) = (10, NpcTalkButton.Close);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:0831180610001020$ 
                // - What brings you here?
                return default;
            case 1:
                // $script:0831180610001023$ 
                // - You look a right mess! How about I treat you? It'll only be a measly $paneltyPrice$ mesos.
                //   Don't worry, I'm a real doctor!
                return default;
            case 10:
                // $script:0831180610001024$ 
                // - You don't look like you need my help right now, but you will eventually. Oh yes, trust me on this one. Bad things happen around here all the time. 
                return default;
        }
        
        return default;
    }
}
