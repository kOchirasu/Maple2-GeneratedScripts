using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000584: Dofio
/// </summary>
public class _11000584 : NpcScript {
    internal _11000584(INpcScriptContext context) : base(context) {
        // TODO: Condition $script:0831180610000841$
        // Id = 1;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000838$ 
                // - What brings you here?
                return true;
            case 1:
                // $script:0831180610000841$ 
                // - You look a right mess! How about I treat you? It'll only be a measly $paneltyPrice$ mesos.
                //   Don't worry, I'm a real doctor!
                return true;
            case 10:
                // $script:0831180610000842$ 
                // - You don't look like you need my help right now, but you will eventually. Oh yes, trust me on this one. Bad things happen around here all the time. 
                return true;
            default:
                return true;
        }
    }
}