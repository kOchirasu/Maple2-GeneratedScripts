using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001484: Lilia
/// </summary>
public class _11001484 : NpcScript {
    internal _11001484(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0201104307005858$ 
                // - Did you come to see me? 
                return true;
            case 30:
                // $script:0201104307005861$ 
                // - Do you want to know about the events we're running right now? Feel free to ask me all about 'em! 
                // $script:0201104607005858$ 
                // - If I have any info to share about events, I'll let you know. 
                return true;
            default:
                return true;
        }
    }
}
