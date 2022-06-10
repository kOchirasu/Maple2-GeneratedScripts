using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000201: Noel
/// </summary>
public class _11000201 : NpcScript {
    internal _11000201(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000874$ 
                // - Hello. 
                return true;
            case 30:
                // $script:0831180407000877$ 
                // - Hey $male:mister,female:lady$, do you want to play with us too? I have to play while I can. My mom will be here soon to pick me up. 
                return true;
            case 40:
                // $script:0831180407000878$ 
                // - I can't believe how big this field is! The sunlight stings a little bit, but Mom said a little sun is good for you. 
                // $script:0831180407000879$ 
                // - $map:02000023$ is nice and shady. Neal's going to come over to my house later. $male:Mister,female:Lady$, do you want to come? 
                return true;
            default:
                return true;
        }
    }
}
