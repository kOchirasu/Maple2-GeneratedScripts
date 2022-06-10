using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003251: Einos
/// </summary>
public class _11003251 : NpcScript {
    internal _11003251(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50;60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008169$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0403155707008170$ 
                // - We must uncover the secret of darkness before it claims any more lives.
                return true;
            case 40:
                // $script:0526174607008529$ 
                // - In search of $itemPlural:20000045$, are you?
                switch (selection) {
                    // $script:0526174607008530$
                    // - Do you have any $itemPlural:20000045$ for me?
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0526174607008531$
                    // - How do I make the crystal react?
                    case 1:
                        Id = 42;
                        return false;
                }
                return true;
            case 41:
                // $script:0526174607008532$ functionID=1 
                // - Here you go. The crystal should react to this.
                return true;
            case 42:
                // $script:0530154407008539$ 
                // - Take the $item:20000045$ to the crystal, then press space.
                return true;
            case 50:
                // $script:0530154407008540$ 
                // - One $item:20000045$ is enough, I think. You don't need any more.
                return true;
            case 60:
                // $script:0530154407008541$ 
                // - We must uncover the secret of darkness before it claims any more lives.
                return true;
            default:
                return true;
        }
    }
}
