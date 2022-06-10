using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003054: Allon
/// </summary>
public class _11003054 : NpcScript {
    internal _11003054(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0102155907007617$ 
                // - What brings you here? 
                return true;
            case 30:
                // $script:0102155907007620$ 
                // - Ah, $MyPCName$. I've been waiting for you.  
                // $script:0102155907007621$ 
                // - This place is cold... desolate. 
                return true;
            default:
                return true;
        }
    }
}
