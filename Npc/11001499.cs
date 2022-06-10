using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001499: Dunba
/// </summary>
public class _11001499 : NpcScript {
    internal _11001499(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0118150907005832$ 
                // - Hello!
                return true;
            case 30:
                // $script:0118150907005835$ 
                // - Do you happen to know where I can find $map:02010053$? It's got to be around here somewhere.
                switch (selection) {
                    // $script:0120134507005846$
                    // - Why do you ask?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0120134507005847$ 
                // - I heard they're holding a big grand opening event. Anyone who brings in this handout gets all they can eat for just 5,000 mesos.
                switch (selection) {
                    // $script:0120134507005848$
                    // - It's right up this escalator!
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0120134507005849$ 
                // - Aw man, the escaltor is out. I didn't sign up for <i>stairs</i>...
                return true;
            default:
                return true;
        }
    }
}
