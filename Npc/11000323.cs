using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000323: Tony
/// </summary>
public class _11000323 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50;60;70
    }

    // Select 0:
    // $script:0831180407001300$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407001303$
                // - I hate history the most. There are too many things to remember, heroes and names and... What was the name of that big-shot warrior? 
                return -1;
            case (50, 0):
                // $script:0831180407001304$
                // - I hate history the most. There are too many things to remember, heroes and names and... What was the name of that big-shot mage? 
                return -1;
            case (60, 0):
                // $script:0831180407001305$
                // - I hate history the most. There are too many things to remember, heroes and names and... What was the name of that big-shot archer? 
                return -1;
            case (70, 0):
                // $script:0831180407001306$
                // - I hate history the most. There are too many things to remember, heroes and names and... What was the name of that big-shot thief? 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.Close,
            (70, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
