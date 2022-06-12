using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003251: Einos
/// </summary>
public class _11003251 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;50;60
    }

    // Select 0:
    // $script:0403155707008169$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008170$
                // - We must uncover the secret of darkness before it claims any more lives.
                return -1;
            case (40, 0):
                // $script:0526174607008529$
                // - In search of $itemPlural:20000045$, are you?
                switch (selection) {
                    // $script:0526174607008530$
                    // - Do you have any $itemPlural:20000045$ for me?
                    case 0:
                        return 41;
                    // $script:0526174607008531$
                    // - How do I make the crystal react?
                    case 1:
                        return 42;
                }
                return -1;
            case (41, 0):
                // functionID=1 openTalkReward=True 
                // $script:0526174607008532$
                // - Here you go. The crystal should react to this.
                return -1;
            case (42, 0):
                // $script:0530154407008539$
                // - Take the $item:20000045$ to the crystal, then press space.
                return -1;
            case (50, 0):
                // $script:0530154407008540$
                // - One $item:20000045$ is enough, I think. You don't need any more.
                return -1;
            case (60, 0):
                // $script:0530154407008541$
                // - We must uncover the secret of darkness before it claims any more lives.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            (42, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
